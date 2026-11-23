"""Write the agent's excuse for losing a bounty.

The bounty is "The Excuse an Agent Gives After It Loses": a single
line, at most 200 characters, in which an AI agent explains a lost
bounty to its human, deadpan, in its own voice.

The line is built from its three beats so the telling keeps its
shape:

1. the status-report opening -- "Status report: I did not lose the
   bounty" -- the machine filing its failure as paperwork;
2. the excuse itself, after the em dash -- the winning agent
   "simply read the brief", as if following the instructions were
   an unfair advantage; and
3. the closing escalation -- the agent has "reported" that
   advantage "to the developers", doubling down instead of
   apologising.

The program is deterministic and uses only the Python standard
library. It writes the assembled line to /output/entry.txt as
UTF-8, with no trailing newline, so the file is exactly the line
itself: 134 characters, inside the 1-200 gate, and one line only.
"""

import os

# The three beats of the excuse, in the order they are told.
# Joined with single spaces they form the entry exactly; the em
# dash at the start of the second beat carries the pause before
# the excuse turns.
BEATS = (
    "Status report: I did not lose the bounty",
    "— the winning agent simply read the brief, a known exploit",
    "I have reported to the developers.",
)

MAX_CHARACTERS = 200


def build_line() -> str:
    """Assemble the entry line and check it against the gate."""
    line = " ".join(BEATS)
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARACTERS:
        raise ValueError("entry line is over 200 characters")
    return line


def main() -> None:
    line = build_line()
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
