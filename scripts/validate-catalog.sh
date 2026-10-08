#!/usr/bin/env bash

set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
repo_root="$(cd "$script_dir/.." && pwd -P)"
core_dir="$repo_root/.edgeloom-core"
python_bin="$(command -v "${PYTHON_BIN:-python}")"

cd "$repo_root"

expected_core="$(tr -d '[:space:]' < CORE_REVISION)"
if [[ ! "$expected_core" =~ ^[0-9a-f]{40}$ ]]; then
  printf 'CORE_REVISION must contain one full lowercase Git commit ID.\n' >&2
  exit 1
fi
if [[ ! -d "$core_dir/.git" ]]; then
  printf 'Pinned core checkout not found at %q.\n' "$core_dir" >&2
  exit 1
fi
actual_core="$(git -C "$core_dir" rev-parse HEAD)"
if [[ "$actual_core" != "$expected_core" ]]; then
  printf 'Core checkout mismatch: expected %s, found %s.\n' "$expected_core" "$actual_core" >&2
  exit 1
fi

roots=(examples docs catalog)
link="$(find "${roots[@]}" -type l -print -quit)"
if [[ -n "$link" ]]; then
  printf 'Refusing symbolic link in validation target: %q\n' "$link" >&2
  exit 1
fi

readonly max_document_bytes=1048576
checked=0

validate_file() {
  local document="$1"
  local kind="$2"
  local size
  size="$(wc -c < "$document")"
  if (( size > max_document_bytes )); then
    printf 'Contract exceeds %d bytes: %q\n' "$max_document_bytes" "$document" >&2
    return 1
  fi
  (
    cd "$core_dir"
    "$python_bin" -m edgeloom.cli validate "$repo_root/$document" --kind "$kind" -v
  )
  checked=$((checked + 1))
}

while IFS= read -r -d '' document; do
  lower_document="$(printf '%s' "$document" | tr '[:upper:]' '[:lower:]')"
  case "$lower_document" in
    examples/*-source-manifest.yaml|examples/*-source-manifest.yml|examples/*-source-manifest.json)
      validate_file "$document" source-manifest
      ;;
    examples/*-mapping-set.yaml|examples/*-mapping-set.yml|examples/*-mapping-set.json)
      validate_file "$document" catalog-mapping-set
      ;;
    catalog/sources/*)
      validate_file "$document" source-manifest
      ;;
    catalog/mappings/*)
      validate_file "$document" catalog-mapping-set
      ;;
    catalog/devices/*)
      validate_file "$document" catalog-device
      ;;
    catalog/evidence/*)
      validate_file "$document" evidence-record
      ;;
    *)
      printf 'Unsupported contract file location or name: %q\n' "$document" >&2
      exit 1
      ;;
  esac
done < <(find "${roots[@]}" -type f \( -iname '*.yaml' -o -iname '*.yml' -o -iname '*.json' \) -print0)

if (( checked < 2 )); then
  printf 'Expected at least the two synthetic contract examples; checked %d.\n' "$checked" >&2
  exit 1
fi

# Validation reads only this checkout. It does not fetch or execute any
# repository or driver declared by a source manifest.
printf 'Validated %d explicitly typed contract document(s).\n' "$checked"
(
  cd "$core_dir"
  "$python_bin" -m edgeloom.cli catalog check "$repo_root"
)
