#!/usr/bin/python3
"""Script markdown2html.py that takes an argument 2 strings"""
import sys
import os


args = sys.argv
if len(args) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)
if not os.path.exists(sys.argv[1]):
    print("Missing {}".format(sys.argv[1]), file=sys.stderr)
    sys.exit(1)
sys.exit(0)
