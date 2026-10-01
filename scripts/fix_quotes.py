# -*- coding: utf-8 -*-
"""Safely convert paired straight double quotes in TEXT NODES to Chinese curly
quotes ("..." -> "..."), for gzh HTML that failed the half-width punctuation
check.

Usage:
    python fix_quotes.py <html_file>

Safety features (each born from a real incident, see SKILL.md Gotchas):
- Only text nodes are processed (document split on tags); tag attributes are
  never touched.
- Only PAIRED quotes are converted. Lone straight quotes are reported, not
  blind-replaced.
- Text inside monospace code blocks is skipped.
- After conversion, content preservation is verified: the plain text with all
  quote characters stripped must be byte-identical to before. This is the
  check that catches silent content loss.
- Control character scan: no chr(0)..chr(31) beyond \\n \\r \\t may remain.

Exit code is non-zero if any check fails or lone quotes were found.
"""
import io
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

MONO_MARKERS = ("monospace", "Consolas", "Courier", "Menlo", "JetBrains")
CODE_BLOCK_RE = re.compile(
    r"<(?:p|section|pre)[^>]*(?:monospace|Consolas|Courier|Menlo|JetBrains)[^>]*>.*?</(?:p|section|pre)>",
    re.DOTALL,
)


def strip_quotes(s: str) -> str:
    for ch in ('"', "\u201c", "\u201d"):
        s = s.replace(ch, "")
    return s


def main(path: str) -> int:
    content = open(path, encoding="utf-8").read()

    # Blank out code-block regions so their quotes are left alone.
    code_spans = [(m.start(), m.end()) for m in CODE_BLOCK_RE.finditer(content)]

    def in_code(pos: int) -> bool:
        return any(s <= pos < e for s, e in code_spans)

    parts = re.split(r"(<[^>]+>)", content)
    converted = 0
    lone_contexts = []
    pos = 0
    for i in range(0, len(parts), 2):
        text = parts[i]
        pos += len(parts[i - 1]) if i > 0 else 0
        node_start = pos
        pos += len(text)
        if '"' not in text or in_code(node_start):
            continue
        new_text, n = re.subn(r'"([^"]*)"', "\u201c\\1\u201d", text)
        converted += n
        if '"' in new_text:
            lone_contexts.append(re.sub(r"\s+", " ", new_text).strip()[:70])
        parts[i] = new_text

    result = "".join(parts)

    # ---- integrity checks ----
    ctrl = [hex(ord(c)) for c in result if ord(c) < 32 and c not in "\n\r\t"]
    ok = True
    if ctrl:
        print(f"FAIL: control characters present: {ctrl[:10]}")
        ok = False

    plain_before = strip_quotes(re.sub(r"<[^>]+>", "", content))
    plain_after = strip_quotes(re.sub(r"<[^>]+>", "", result))
    if plain_before != plain_after:
        print("FAIL: text content changed other than quote characters -- aborting, file NOT written")
        return 2

    open_curly, close_curly = result.count("\u201c"), result.count("\u201d")
    if open_curly != close_curly:
        print(f"WARNING: curly quotes unbalanced ({open_curly} open / {close_curly} close)")

    if ok:
        with open(path, "w", encoding="utf-8") as f:
            f.write(result)

    print(f"converted pairs: {converted}")
    print(f"curly quote balance: {open_curly} / {close_curly}")
    print(f"code-block regions skipped: {len(code_spans)}")
    if lone_contexts:
        print(f"WARNING: {len(lone_contexts)} unpaired straight quote(s) left for manual review:")
        for s in lone_contexts:
            print("  -", s)
        return 1
    return 0 if ok else 2


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(64)
    sys.exit(main(sys.argv[1]))
