#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
output="$script_dir/IN3050-4050-Group2-main.zip"

cat "$script_dir"/full-zip/IN3050-4050-Group2-main.zip.part-* > "$output"

echo "Created: $output"
echo "Expected SHA-256: 03cbf631f5d6bfc1582d7a573e1ea3e94831d929884c907175a295c7b3314f61"
sha256sum "$output" 2>/dev/null || shasum -a 256 "$output"
