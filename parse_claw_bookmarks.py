#!/usr/bin/env python3

import json

out = open("LobstersLinks.md", "w")

out.write(
    """---
title: "Lobste.rs Links"
date: "2001-03-25"
---\n
"""
)


with open("static/claw-export.json", "r") as f:
    json = json.loads("\n".join(f.readlines()))
    for row in json:
        out.write(
            """- [{}]({}) , [Lobste.rs Discussion]({})\n""".format(
                row["title"],
                row["url"] if row["url"] != "" else row["comments_url"],
                row["comments_url"],
            )
        )
