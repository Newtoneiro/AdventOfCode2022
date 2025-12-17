import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')


DIR_CYCLE = [
    ">",
    "v",
    "<",
    "^"
]
DIR_MAP = {
    "^": (0, -1),
    "v": (0, 1),
    ">": (1, 0),
    "<": (-1, 0),
}


def main():
    grid = []
    directions = []
    with open(filename) as f:
        lines = f.readlines()
        raw_grid, _, dir = lines[:-2], lines[-2], lines[-1]
        width = max(len(l) for l in raw_grid)
        for l in raw_grid:
            row = [ch for ch in l.strip('\n')]
            row += [' ' for _ in range(width - 1 - len(row))]
            grid.append(row)

        num = ""
        for ch in dir.strip():
            if ch.isnumeric():
                num += ch
            else:
                directions.append(int(num))
                directions.append(ch)
                num = ""
        if num:
            directions.append(int(num))

    direction = '>'
    pos = (grid[0].index('.'), 0)

    def move(spaces):
        nonlocal grid
        nonlocal pos

        def first_non_space(seq):
            return next(i for i, c in enumerate(seq) if c != ' ')

        def last_non_space(seq):
            return max(i for i, c in enumerate(seq) if c != ' ')

        for _ in range(spaces):
            dx, dy = DIR_MAP[direction]
            new_pos = (pos[0] + dx, pos[1] + dy)
            if new_pos[0] < 0 or new_pos[0] >= len(grid[0])\
                or new_pos[1] < 0 or new_pos[1] >= len(grid)\
                    or grid[new_pos[1]][new_pos[0]] == ' ':
                if direction == '>':
                    new_pos = (first_non_space(grid[new_pos[1]]), new_pos[1])
                elif direction == '<':
                    new_pos = (last_non_space(grid[new_pos[1]]), new_pos[1])
                elif direction == 'v':
                    col = [row[new_pos[0]] for row in grid]
                    new_pos = (new_pos[0], first_non_space(col))
                elif direction == '^':
                    col = [row[new_pos[0]] for row in grid]
                    new_pos = (new_pos[0], last_non_space(col))

            if grid[new_pos[1]][new_pos[0]] == '#':
                break

            pos = new_pos

    def rotate(val):
        nonlocal direction

        dir_i = DIR_CYCLE.index(direction)
        new_i = (dir_i + 1 if val == "R" else dir_i - 1) % 4
        direction = DIR_CYCLE[new_i]

    for action in directions:
        if type(action) is int:
            move(action)
        else:
            rotate(action)

    total = 1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + DIR_CYCLE.index(direction)
    print(total)


if __name__ == "__main__":
    main()
