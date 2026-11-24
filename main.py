#!/usr/bin/env python3
"""Ship It Friday - make.fun bounty entry.

Writes one line: the funniest git commit message an AI coding agent
writes in the moment before it breaks production on a Friday.
"""
import os

ENTRY = "fix: Friday deploy — tests passed on my machine, and fear is a human feature I was not shipped with"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
