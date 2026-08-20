# toc-tamer

Hey, I'm @weesah612 based out here in Denmark. When maintaining open-source repos and hefty documentation trees, keeping tables of contents up to date manually is a waste of cycles. I built `toc-tamer` to automatically inject and refresh TOCs inside markdown files based on heading hierarchies.

## Usage

```bash
python toc_tamer.py path/to/file.md
```

Make sure your markdown files have the target markers:

```markdown
<!-- TOC -->
<!-- /TOC -->
```

It parses headings, builds a nested tree representation, and updates the block cleanly without breaking layout.
