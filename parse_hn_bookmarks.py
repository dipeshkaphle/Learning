#!/usr/bin/env python3

from typing import List


def chunks(l: List[str], n: int):
    for i in range(0, len(l), n):
        yield [l[j] for j in range(i, min(i + n, len(l)))]


out = open("HNLinks.md", "w")

out.write(
    """---
title = "HN Links"
date = "2001-03-25"
---\n
"""
)

with open("static/materialistic-export.txt", "r") as f:
    lines = f.readlines()
    for chnk in chunks(lines, 4):
        out.write(
            """- [{}]({}) , [HN Discussion]({})\n""".format(
                chnk[0].strip(), chnk[1].strip(), chnk[2].strip()
            )
        )
