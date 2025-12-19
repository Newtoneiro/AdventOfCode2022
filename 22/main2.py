import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")


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
MAP_LAYOUT = [
    [0, 1, 2],
    [0, 3, 0],
    [5, 4, 0],
    [6, 0, 0],
]


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

    SIDE = (width) // 3
    faces = {}
    origin = {}
    for fy, row in enumerate(MAP_LAYOUT):
        y0 = fy * SIDE
        for fx, fid in enumerate(row):
            x0 = fx * SIDE
            if fid:
                faces[fid] = [grid[y0 + i][x0: x0 + SIDE] for i in range(SIDE)]
                origin[fid] = (x0, y0)

    T = {
        (1, "^"): (6, ">", lambda x, y: (0, x)),
        (1, "<"): (5, ">", lambda x, y: (0, SIDE - 1 - y)),
        (1, ">"): (2, ">", lambda x, y: (0, y)),
        (1, "v"): (3, "v", lambda x, y: (x, 0)), 
        (2, "^"): (6, "^", lambda x, y: (x, SIDE - 1)),
        (2, ">"): (4, "<", lambda x, y: (SIDE - 1, SIDE - 1 - y)),
        (2, "v"): (3, "<", lambda x, y: (SIDE - 1, x)),
        (2, "<"): (1, "<", lambda x, y: (SIDE - 1, y)),
        (3, "^"): (1, "^", lambda x, y: (x, SIDE - 1)),
        (3, "<"): (5, "v", lambda x, y: (y, 0)),
        (3, ">"): (2, "^", lambda x, y: (y, SIDE - 1)),
        (3, "v"): (4, "v", lambda x, y: (x, 0)),
        (4, "^"): (3, "^", lambda x, y: (x, SIDE - 1)),
        (4, "<"): (5, "<", lambda x, y: (SIDE - 1, y)),
        (4, ">"): (2, "<", lambda x, y: (SIDE - 1, SIDE - 1 - y)),
        (4, "v"): (6, "<", lambda x, y: (SIDE - 1, x)),
        (5, "^"): (3, ">", lambda x, y: (0, x)),
        (5, "<"): (1, ">", lambda x, y: (0, SIDE - 1 - y)),
        (5, ">"): (4, ">", lambda x, y: (0, y)),
        (5, "v"): (6, "v", lambda x, y: (x, 0)),
        (6, "^"): (5, "^", lambda x, y: (x, SIDE - 1)),
        (6, "<"): (1, "v", lambda x, y: (y, 0)),
        (6, ">"): (4, "^", lambda x, y: (y, SIDE - 1)),
        (6, "v"): (2, "v", lambda x, y: (x, 0)),
    }

    cur_face = 1
    direction = ">"
    pos = (0, 0)

    def move(spaces):
        nonlocal faces
        nonlocal cur_face
        nonlocal direction
        nonlocal pos

        for _ in range(spaces):
            dx, dy = DIR_MAP[direction]
            new_face = cur_face
            new_direction = direction
            new_pos = (pos[0] + dx, pos[1] + dy)

            if new_pos[0] < 0 or new_pos[0] >= SIDE\
                    or new_pos[1] < 0 or new_pos[1] >= SIDE:
                new_face, new_direction, transition = T[(new_face, new_direction)]
                new_pos = transition(new_pos[0], new_pos[1])

            if faces[new_face][new_pos[1]][new_pos[0]] == '#':
                break

            cur_face = new_face
            direction = new_direction
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

    origin_pos = (pos[0] + origin[cur_face][0], pos[1] + origin[cur_face][1])
    total = 1000 * (origin_pos[1] + 1) + 4 * (origin_pos[0] + 1) + DIR_CYCLE.index(direction)
    print(total)


if __name__ == "__main__":
    main()
