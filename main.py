#!/usr/bin/env python3
"""Write one short, funny rant about reply-all to /output/entry.txt.

Competition: Angry Judge - The Short Rant Contest
(u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

The rant targets one everyday annoyance - the colleague who hits
reply-all with "Thanks!" - and escalates from mild irritation to
full fury, landing the punch on what the email was actually about.
"""

import os

RANT = (
    "One person hits reply-all with 'Thanks!' and suddenly 400 strangers "
    "are replying 'Thanks!' back, like a choir of people who can't "
    "read. I now have 87 unread emails. Eighty-six are colleagues "
    "thanking each other. The last one is IT begging us to stop. STOP. "
    "All this over a broken kettle."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # Write the rant verbatim: no trailing newline, so the file
    # contains exactly RANT and nothing else.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(RANT)


if __name__ == "__main__":
    main()
