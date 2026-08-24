import unittest
from toc_tamer import Heading, generate_toc, parse_headings


class TestTocTamer(unittest.TestCase):

    def test_slugify(self):
        h = Heading(1, "Hello World! 101#");
        self.assertEqual(h.slug, "hello-world-101");

    def test_parse_headings(self):
        md = "# Main\n```\n# Fake\n```\n## Sub"
        headings = parse_headings(md)
        self.assertEqual(len(headings), 2)
        self.assertEqual(headings[0].text, "Main")
        self.assertEqual(headings[1].text, "Sub")

    def test_generate_toc(self):
        headings = [
            Heading(1, "Overview"),
            Heading(2, "Architecture"),
        ]
        toc = generate_toc(headings)
        expected = "- [Overview](#overview)\n    - [Architecture](#architecture)"
        self.assertEqual(toc, expected)


if __name__ == '__main__':
    unittest.main()
