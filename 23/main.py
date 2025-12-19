import os
from collections import defaultdict, deque


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

DIR_MAP = {
    "N":  (0, -1),
    "NE": (1, -1),
    "E":  (1, 0),
    "SE": (1, 1),
    "S":  (0, 1),
    "SW": (-1, 1),
    "W":  (-1, 0),
    "NW": (-1, -1),
}
MOVES = deque([
    (["N", "NE", "NW"], "N"),
    (["S", "SE", "SW"], "S"),
    (["W", "NW", "SW"], "W"),
    (["E", "NE", "SE"], "E"),
])
ROUNDS = 10


def main():
    elves = set()
    with open(filename) as f:
        for y, line in enumerate(f.readlines()):
            for x, char in enumerate(line.strip()):
                if char == "#":
                    elves.add((x, y))

    def normalize(coords):
        min_x = min(x for x, y in coords)
        min_y = min(y for x, y in coords)

        return {(x - min_x, y - min_y) for x, y in coords}

    for _ in range(ROUNDS):
        propositions = defaultdict(set)
        for (x, y) in elves:
            if not any(
                (x + dx, y + dy) in elves
                for dx, dy in DIR_MAP.values()
            ):
                propositions[(x, y)].add((x, y))
                continue

            moved = False
            for forbidden, direction in MOVES:
                if not any(
                    (x + dx, y + dy) in elves
                    for dir in forbidden
                    for dx, dy in [DIR_MAP[dir]]
                ):
                    dx, dy = DIR_MAP[direction]
                    new_x, new_y = x + dx, y + dy
                    propositions[(new_x, new_y)].add((x, y))
                    moved = True
                    break

            if not moved:
                propositions[(x, y)].add((x, y))

        new_elves = set()
        for new, prevs in propositions.items():
            if len(prevs) == 1:
                new_elves.add(new)
            else:
                new_elves.update(prevs)
        elves = new_elves

        MOVES.rotate(-1)

    normalized = normalize(new_elves)
    width = max(x for x, y in normalized)
    height = max(y for x, y in normalized)
    total = (width + 1) * (height + 1) - len(normalized)

    print(total)


if __name__ == "__main__":
    main()
