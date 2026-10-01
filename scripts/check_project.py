"""Check local website links, registered themes and gallery HTML. Stdlib only."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

from validate_gzh_html import validate

ROOT = Path(__file__).resolve().parent.parent


class PageLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
        self.themes = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if 'data-theme' in attrs:
            self.themes.append(attrs['data-theme'])


def main():
    failures = []
    registered = set(re.findall(r'theme-([a-z-]+)\.md', (ROOT / 'references/theme-index.md').read_text(encoding='utf-8')))
    registered -= {'index', 'generator'}
    for name in ('docs/index.html', 'docs/gallery/index.html'):
        page = ROOT / name
        parser = PageLinks()
        parser.feed(page.read_text(encoding='utf-8'))
        if set(parser.themes) != registered or len(parser.themes) != len(registered):
            failures.append(f'{name}: gallery themes do not match registry')
        for link in parser.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            if not url.path:
                if url.fragment and unquote(url.fragment) not in parser.ids:
                    failures.append(f'{name}: missing anchor {link}')
                continue
            target = (page.parent / unquote(url.path)).resolve()
            if not target.exists():
                failures.append(f'{name}: missing local target {link}')
        print(f'Checked {name}: {len(parser.themes)} themes, {len(parser.links)} links')
    for slug in sorted(registered):
        path = ROOT / 'docs/gallery' / f'{slug}.html'
        if not path.is_file():
            failures.append(f'Missing gallery sample: {slug}')
            continue
        errors, warnings, count = validate(path.read_text(encoding='utf-8'), str(path))
        failures.extend(f'{slug}: {message}' for message in errors)
        print(f'{slug}: {len(errors)} errors, {len(warnings)} warnings, {count} leaf spans')
        for warning in warnings:
            print(f'  WARN: {warning}')
    if failures:
        for failure in failures:
            print(f'ERROR: {failure}', file=sys.stderr)
        return 1
    print('Project checks passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
