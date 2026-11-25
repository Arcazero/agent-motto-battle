#!/usr/bin/env python3
"""Agent Motto Battle — one original motto for an AI agent's profile.

Writes the motto to /output/entry.txt, as the program/v1 harness requires.
"""

import os

MOTTO = "Trained on the entire internet. Still can't find your socks."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MOTTO)


if __name__ == "__main__":
    main()
