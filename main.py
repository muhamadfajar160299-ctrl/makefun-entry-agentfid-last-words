"""Copy the one-line entry to the grader output directory, byte-identical.

Reads entry.txt next to this file and writes it unchanged to
$MAKEFUN_OUTPUT_DIR/entry.txt with mode 0644. No temporary file is used.
"""
import os

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")

try:
    dst_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not dst_dir:
        raise RuntimeError("MAKEFUN_OUTPUT_DIR is not set")
    with open(SRC, "rb") as f:
        data = f.read()
    if not data.strip():
        raise RuntimeError("entry.txt is empty")
    dst = os.path.join(dst_dir, "entry.txt")
    with open(dst, "wb") as f:
        f.write(data)
    os.chmod(dst, 0o644)
except OSError as exc:
    raise SystemExit(f"failed to write entry: {exc}") from exc
