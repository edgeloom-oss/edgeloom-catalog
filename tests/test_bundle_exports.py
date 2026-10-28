import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "bundle_exports",
    Path(__file__).resolve().parents[1] / "scripts/check-bundle-exports.py",
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class BundleInventoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.directory = self.root / "catalog/bundles"
        self.directory.mkdir(parents=True)

    def record(self, filename, identifier="demo", kind="device-evidence-bundle"):
        (self.directory / filename).write_text(
            json.dumps({"id": identifier, "kind": kind})
        )

    def test_all_formats_and_sorted_inventory(self):
        self.record("z.json", "second")
        self.record("a.yaml", "first")
        self.record("b.yml", "third")
        (self.directory / "README.md").write_text("Not a record")
        self.assertEqual(MODULE.bundle_ids(self.root), ["first", "third", "second"])

    def test_empty_rejected(self):
        with self.assertRaises(ValueError):
            MODULE.bundle_ids(self.root)

    def test_duplicate_rejected(self):
        self.record("a.json")
        self.record("b.json")
        with self.assertRaises(ValueError):
            MODULE.bundle_ids(self.root)

    def test_unsafe_id_rejected(self):
        for identifier in ("../escape", "--flag", "Demo", "a/b", ""):
            with self.subTest(identifier=identifier):
                self.record("a.json", identifier)
                with self.assertRaises(ValueError):
                    MODULE.bundle_ids(self.root)

    def test_wrong_kind_rejected(self):
        self.record("a.json", kind="catalog-device")
        with self.assertRaises(ValueError):
            MODULE.bundle_ids(self.root)

    def test_symlink_rejected(self):
        self.record("a.json")
        (self.directory / "b.json").symlink_to(self.directory / "a.json")
        with self.assertRaises(ValueError):
            MODULE.bundle_ids(self.root)

    def test_oversized_rejected(self):
        (self.directory / "a.json").write_text(" " * 1048577)
        with self.assertRaises(ValueError):
            MODULE.bundle_ids(self.root)
