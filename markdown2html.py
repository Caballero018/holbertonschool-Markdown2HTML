#!/usr/bin/python3
"""Script markdown2html.py that takes an argument 2 strings"""
import sys
import os


def md_to_html(markdown, html):
    """Function that parses the Headings Markdown syntax to generate HTML."""

    "Read markdown file"
    with open(markdown) as f:
        lines = f.readlines()

    for line in lines:
        hash = txt = ''
        for character in line:
            "Number of hash"
            if character == '#':
                hash += character
            "Text without numerals"
            if character != '#':
                txt += character

        "Write in html file"
        with open(html, 'a') as f:
            if len(character) > 0 and len(hash) > 0:
                f.write("<h{len_h}>{txt}</h{len_h}>\n".format(
                    len_h=len(hash), txt=txt[1:-1]
                    ))


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)
    if not os.path.exists(args[1]):
        print("Missing {}".format(args[1]), file=sys.stderr)
        sys.exit(1)

    md_to_html(args[1], args[2])

    sys.exit(0)
