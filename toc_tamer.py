import re
import sys


class Heading:
    def __init__(self, level, text):
        self.level = level
        self.text = text
        self.slug = self._slugify(text)

    def _slugify(self, text):
        slug = text.lower()
        slug = re.sub(r'[^a-z0-9-_\s]', '', slug)
        slug = re.sub(r'\s+', '-', slug)
        return slug


def parse_headings(content):
    # Ignore code blocks to avoid grabbing headers inside examples
    lines = content.splitlines()
    headings = []
    in_code_block = False

    for line in lines:
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue

        if not in_code_block:
            match = re.match(^(#{1,6})\s+(.+)$',
            if match:
                level = len(match.group(1))
                text = match.group(2).strip()
                headings.append(Heading(level, text))

    return headings


def generate_toc(headings):
    if not headings:
        return ""

    min_level = min(h.level for h in headings)
    toc_lines = []

    for h in headings:
        indent_level = h.level - min_level
        indent = "    " * indent_level
        toc_lines.append(f"{indent}- [{h.text}](#{h.slug})")

    return "\n".join(toc_lines)


def refresh_toc(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    headings = parse_headings(content)
    new_toc = generate_toc(headings)

    start_marker = "<!-- TOC -->"
    end_marker = "<!-- /TOC -->"

    pattern = re.compile(
        f"{re.escape(start_marker)}.*?{re.escape(end_marker)}", re.DOTALL
    )

    replacement = f"{start_marker}\n{new_toc}\n{end_marker}"

    if not pattern.search(content):
        print(f"Error: Markers {start_marker} and {end_marker} not found in {file_path}")
        sys.exit(1)

    updated_content = pattern.sub(replacement, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"Successfully refreshed TOC in {file_path}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python toc_tamer.py <markdown_file>")
        sys.exit(1)

    refresh_toc(sys.argv[1])
