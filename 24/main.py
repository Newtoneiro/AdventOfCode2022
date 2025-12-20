import os
from math import lcm
from collections import deque

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

DIR_MAP = {
    "^": (0, -1),
    "v": (0, 1),
    ">": (1, 0),
    "<": (-1, 0),
}


def main():
    blizzards = []
    grid = []
    with open(filename) as f:
        for y, line in enumerate(f.readlines()):
            row = []
            for x, char in enumerate(line.strip()):
                if char in [">", "v", "<", "^"]:
                    blizzards.append((char, (x, y)))
                    row.append('.')
                else:
                    row.append(char)
            grid.append(row)

    width, height = x + 1, y + 1
    PERIOD = lcm(width - 2, height - 2)

    BLIZZARD_DIC = {}
    BLIZZARD_DIC[0] = set(blizzards)

    for i in range(1, PERIOD):
        prev = BLIZZARD_DIC[i - 1]
        new_blizzards = set()

        for dir, (x, y) in prev:
            dx, dy = DIR_MAP[dir]
            nx, ny = x + dx, y + dy

            if nx == 0:
                nx = width - 2
            elif nx == width - 1:
                nx = 1

            if ny == 0:
                ny = height - 2
            elif ny == height - 1:
                ny = 1

            new_blizzards.add((dir, (nx, ny)))

        BLIZZARD_DIC[i] = new_blizzards

    BLIZZARD_DIC = {k: set(t[1] for t in v) for k, v in BLIZZARD_DIC.items()}

    end = (width - 2, height - 1)

    queue = deque([(1, 0, 0)])
    visited = set([(1, 0, 0)])
    while queue:
        x, y, t = queue.popleft()
        if (x, y) == end:
            print(t)
            return

        next_t = (t + 1) % PERIOD
        blocked = BLIZZARD_DIC[next_t]

        for dx, dy in [(0, 0), *DIR_MAP.values()]:
            nx, ny = x + dx, y + dy

            if (nx, ny) in blocked:
                continue
            if (nx, ny) != (1, 0) and (nx, ny) != end:  # allow start and end
                if nx == 0 or nx == width - 1 or ny == 0 or ny == height - 1:
                    continue

            state = (nx, ny, next_t)
            if state not in visited:
                visited.add(state)
                queue.append((nx, ny, t + 1))


if __name__ == "__main__":
    main()
