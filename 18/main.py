import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')


def main():
    coordinates = []
    with open(filename) as f:
        for line in f:
            coordinates.append(tuple(int(x) for x in line.strip().split(',')))

    def adjacent(a, b):
        dx = abs(a[0] - b[0])
        dy = abs(a[1] - b[1])
        dz = abs(a[2] - b[2])
        return (dx + dy + dz == 1)

    def exposed_sides(cubes):
        total = 0
        for x, y, z in cubes:
            for dx, dy, dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
                if (x+dx, y+dy, z+dz) not in cubes:
                    total += 1
        return total

    groups = []
    for block in coordinates:
        new_group = []
        groups_to_combine = []
        for i, group in enumerate(groups):
            if any(adjacent(block, block2) for block2 in group):
                new_group.extend(group)
                groups_to_combine.append(i)
                new_group.append(block)

        if len(new_group) == 0:
            new_group = [block]

        for i in sorted(groups_to_combine, reverse=True):
            del groups[i]
        groups.append(new_group)

    groups = [set(g) for g in groups]

    print(sum(exposed_sides(group) for group in groups))


if __name__ == "__main__":
    main()
