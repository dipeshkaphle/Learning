#!/usr/bin/env python3

from typing import List
import json

def chunks(l: List[str], n: int):
    for i in range(0, len(l), n):
        yield [l[j] for j in range(i, min(i + n, len(l)))]


out = open("HNLinks.md", "w")

out.write(
    """---
title: "HN Links"
date: "2001-03-25"
---\n
"""
)

# Process materialistic bookmarks
with open("static/materialistic-export-final.txt", "r") as f:
    lines = f.readlines()
    for chnk in chunks(lines, 4):
        if len(chnk) >= 3:
            out.write(
                """- [{}]({}) , [HN Discussion]({})\n""".format(
                    chnk[0].strip(), chnk[1].strip(), chnk[2].strip()
                )
            )

# Process harmonic bookmarks
with open("static/harmonic_bookmarks.json", "r") as f:
    harmonic_data = json.load(f)
    for item in harmonic_data:
        out.write(
            f"- [{item['title']}]({item['url']}) , [HN Discussion]({item['hn_link']})\n"
        )

out.close()

print("Successfully updated HNLinks.md with bookmarks from both sources.")
