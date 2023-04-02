#!/usr/bin/python3
"""Script markdown2html.py that takes an argument 2 strings"""
import sys
import os


def headings(line, html):
    """Function that parses the Headings Markdown syntax to generate HTML."""
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


def unordered_list(line, html):
    """Function that parses unordered listing syntax for generating HTML"""
    li = txt = ''
    for character in line:
        "Number of li"
        if character == '-':
            li += character
        "Text without numerals"
        if character != '-':
            txt += character

    if len(li) > 0 and len(txt) > 0:
        with open(html, 'a') as f:
            "Write in html file"
            f.write("<li>{txt}</li>\n".format(txt=txt[1:-1]))


def switch(lines, html):
    """Switch in the case"""
    ul = closed_ul = 0
    for i in range(len(lines)):
        "Case headings"
        if lines[i][0] == '#':
            headings(lines[i], html)

        "Case unordered list"
        if lines[i][0] == '-':
            if i > 0:
                try:
                    if lines[i - 1][0] != '-' or lines[i + 1][0] != '-':
                        ul = 0
                    if lines[i + 1] == '\n':
                        ul = 1
                    if lines[i + 1][0] != '-':
                        closed_ul = 1
                except IndexError:
                    i = len(lines) - 1
            if ul == 0:
                with open(html, 'a') as f:
                    "Write in html file"
                    f.write("<ul>\n")
            unordered_list(lines[i], html)
            if closed_ul == 1:
                with open(html, 'a') as f:
                    "Write in html file"
                    f.write("</ul>\n")
            ul = 1
            closed_ul = 0
    if lines[i][0] == '-':
        with open(html, 'a') as f:
            "Write in html file"
            f.write("</ul>\n")


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)
    if not os.path.exists(args[1]):
        print("Missing {}".format(args[1]), file=sys.stderr)
        sys.exit(1)

    "Read markdown file"
    with open(args[1]) as f:
        lines = f.readlines()

    switch(lines, args[2])

    sys.exit(0)
