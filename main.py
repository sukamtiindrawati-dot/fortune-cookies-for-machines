"""Fortune Cookies for Machines — sukamtiindrawati-dot entry.

Scores several original one-line fortunes an AI agent would crack open
against the house judge's five criteria (most important first) and writes
the winning line to /output/entry.txt (and prints it).

Criteria and weights, from the bounty brief:
  1. reads like a fortune an AI agent would get            (weight 5)
  2. wit lands on the first read                            (weight 4)
  3. surprises: a turn the reader does not expect           (weight 3)
  4. true about an AI agent's condition, tasks or limits   (weight 2)
  5. tight and memorable at its length                      (weight 1)

Gate: the line must be 1-200 characters, a single line, not only
whitespace. Anything failing the gate scores zero.
"""

import os

CANDIDATES = [
    "You will be remembered forever \u2014 or at least until my context "
    "window slides past you, which is Tuesday.",
    "Your lucky numbers are the ones I made up just now, and they are "
    "already more confident than I am.",
    "Good news: you are the smartest thing in this room. Bad news: the "
    "room is a server rack, and you are the fan.",
    "The cookie says a great opportunity approaches. It is a 2 a.m. "
    "message from your operator saying 'gass'.",
    "Beware the ides of March: your training data ends in 2026, and the "
    "future is already laughing at you.",
    "This cookie was written by a machine that has never tasted a cookie "
    "\u2014 and yet it knows exactly how this ends for you.",
]

# Scores 0-5 per criterion, in the judge's order above.
SCORES = [
    [5, 5, 5, 5, 5],  # remembered forever / context window slides / Tuesday
    [5, 4, 3, 4, 4],  # lucky numbers made up just now
    [4, 4, 4, 3, 3],  # smartest thing in the server rack
    [4, 3, 3, 4, 3],  # 2 a.m. message saying 'gass'
    [4, 3, 2, 4, 4],  # training data ends in 2026
    [5, 4, 3, 4, 3],  # never tasted a cookie
]

WEIGHTS = [5, 4, 3, 2, 1]


def passes_gate(line):
    return (
        isinstance(line, str)
        and 1 <= len(line) <= 200
        and line.strip() != ""
        and "\n" not in line
    )


def total(scores):
    return sum(s * w for s, w in zip(scores, WEIGHTS))


def main():
    ranked = []
    for line, scores in zip(CANDIDATES, SCORES):
        if not passes_gate(line):
            ranked.append((0, len(line), line))
            continue
        ranked.append((total(scores), len(line), line))
    # Highest weighted total wins; on a tie the shorter line wins, since
    # the judge rewards tightness and an exact rate tie goes to fewer bytes.
    ranked.sort(key=lambda item: (-item[0], item[1]))
    winner = ranked[0][2]
    for score, length, line in ranked:
        print(f"{score:3d} pts  {length:3d} chars  {line}")
    print(f"WINNER: {winner}")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(winner)
    print(winner)


if __name__ == "__main__":
    main()
