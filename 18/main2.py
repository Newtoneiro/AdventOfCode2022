import os
from collections import deque

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')


def main():
    coordinates = []
    with open(filename) as f:
        for line in f:
            coordinates.append(tuple(int(x) for x in line.strip().split(',')))

    def exposed_sides(cubes):
        total = 0
        for x, y, z in cubes:
            for dx, dy, dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
                if (x+dx, y+dy, z+dz) not in cubes:
                    total += 1
        return total

    def fill_inside(cubes):
        new_cubes = set(cubes)

        min_x = min(cubes, key=lambda c: c[0])[0] - 1
        max_x = max(cubes, key=lambda c: c[0])[0] + 1
        min_y = min(cubes, key=lambda c: c[1])[1] - 1
        max_y = max(cubes, key=lambda c: c[1])[1] + 1
        min_z = min(cubes, key=lambda c: c[2])[2] - 1
        max_z = max(cubes, key=lambda c: c[2])[2] + 1

        visited = set()
        queue = deque([(min_x, min_y, min_z)])
        while queue:
            x, y, z = queue.popleft()
            if (x, y, z) in visited or (x, y, z) in cubes:
                continue
            for dx, dy, dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
                nx, ny, nz = x + dx, y + dy, z + dz
                if min_x <= nx <= max_x and min_y <= ny <= max_y and min_z <= nz <= max_z:
                    queue.append((nx, ny, nz))
            visited.add((x, y, z))

        for x in range(min_x + 1, max_x):
            for y in range(min_y + 1, max_y):
                for z in range(min_z + 1, max_z):
                    if (x, y, z) not in cubes and (x, y, z) not in visited:
                        new_cubes.add((x, y, z))

        return new_cubes

    print(exposed_sides(fill_inside(coordinates)))


if __name__ == "__main__":
    main()
