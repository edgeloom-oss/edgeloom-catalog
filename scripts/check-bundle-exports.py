"""Check every canonical bundle with the pinned core, without fetching sources."""

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml


def bundle_ids(root):
    directory = root / "catalog" / "bundles"
    found = []
    for path in sorted(directory.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Symlink is not allowed: {path}")
        if path.suffix.lower() not in {".json", ".yaml", ".yml"}:
            continue
        if path.stat().st_size > 1048576:
            raise ValueError(f"Oversized bundle: {path}")
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        if (
            not isinstance(record, dict)
            or record.get("kind") != "device-evidence-bundle"
        ):
            raise ValueError(f"Not a bundle record: {path}")
        identifier = record.get("id")
        if not isinstance(identifier, str) or not re.fullmatch(
            r"[a-z0-9]+(?:-[a-z0-9]+)*", identifier
        ):
            raise ValueError(f"Unsafe bundle ID: {path}")
        if identifier in found:
            raise ValueError(f"Duplicate bundle ID: {identifier}")
        found.append(identifier)
    if not found:
        raise ValueError("No canonical bundles found")
    return found


def check_exports(root):
    root = root.resolve()
    core = root / ".edgeloom-core"
    expected = (root / "CORE_REVISION").read_text().strip()
    actual = subprocess.check_output(
        ["git", "-C", str(core), "rev-parse", "HEAD"], text=True
    ).strip()
    if not re.fullmatch(r"[0-9a-f]{40}", expected) or actual != expected:
        raise ValueError("Pinned core revision mismatch")
    identifiers = bundle_ids(root)
    with tempfile.TemporaryDirectory(prefix="edgeloom-bundle-check-") as temporary:
        for identifier in identifiers:
            outputs = [Path(temporary) / f"{identifier}-{i}.zip" for i in (1, 2)]
            for output in outputs:
                subprocess.run(
                    [
                        sys.executable,
                        "-m",
                        "edgeloom.cli",
                        "bundle",
                        "export",
                        str(root),
                        identifier,
                        "--output",
                        str(output),
                    ],
                    cwd=core,
                    check=True,
                )
            if outputs[0].read_bytes() != outputs[1].read_bytes():
                raise ValueError(f"Non-deterministic bundle export: {identifier}")
            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "edgeloom.cli",
                    "bundle",
                    "verify",
                    str(outputs[0]),
                ],
                cwd=core,
                check=True,
            )
            print(
                f"PASS: {identifier} (repeatable export and offline verification)",
                flush=True,
            )
    print(json.dumps({"checked_bundle_ids": identifiers, "core_revision": expected}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("catalog", type=Path)
    check_exports(parser.parse_args().catalog)
