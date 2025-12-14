import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

rock1 = [(0, 0), (1, 0), (2, 0), (3, 0)]
rock2 = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]
rock3 = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
rock4 = [(0, 0), (0, 1), (0, 2), (0, 3)]
rock5 = [(0, 0), (1, 0), (0, 1), (1, 1)]
rocks = [rock1, rock2, rock3, rock4, rock5]


def main(N):
    jets = []
    with open(filename) as f:
        for line in f:
            for char in line.strip():
                jets.append(char)

    occupied = set((x, 0) for x in range(7))
    cur_jet = 0
    rock_count = 0
    max_y = 0

    seen = {}
    added_height = 0

    while rock_count < N:
        rock = rocks[rock_count % 5]
        x, y = 2, max_y + 4

        while True:
            dx = 1 if jets[cur_jet] == '>' else -1
            cur_jet = (cur_jet + 1) % len(jets)
            if all(0 <= x + dx + part[0] <= 6 and (x + dx + part[0], y + part[1]) not in occupied for part in rock):
                x += dx

            if all((x + part[0], y + part[1] - 1) not in occupied for part in rock):
                y -= 1
            else:
                for part in rock:
                    occupied.add((x + part[0], y + part[1]))
                    max_y = max(max_y, y + part[1])
                break

        N_rows = 30
        top_rows = tuple(sorted(
            (px, max_y - py) for px, py in occupied if max_y - py < N_rows
        ))
        key = (rock_count % 5, cur_jet, top_rows)
        if key in seen and rock_count >= 2022:
            old_count, old_height = seen[key]
            cycle_len = rock_count - old_count
            cycle_height = max_y - old_height
            num_cycles = (N - rock_count) // cycle_len
            added_height += num_cycles * cycle_height
            rock_count += num_cycles * cycle_len
        else:
            seen[key] = (rock_count, max_y)

        rock_count += 1

    return max_y + added_height


if __name__ == "__main__":
    print(main(1000000000000))
