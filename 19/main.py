import os
import re
from functools import lru_cache

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')


def main():
    blueprints = []

    with open(filename) as f:
        for line in f.readlines():
            numbers = tuple(int(x) for x in re.findall(r'\d+', line.strip()))
            blueprints.append({
                "ore_robot": (numbers[1], 0, 0, 0),
                "clay_robot": (numbers[2], 0, 0, 0),
                "obsidian_robot": (numbers[3], numbers[4], 0, 0),
                "geode_robot": (numbers[5], 0, numbers[6], 0)
            })

    def can_create(resources, cost):
        for r, c in zip(resources, cost):
            if r < c:
                return False
        return True

    def subtract(a, b):
        return tuple(a_v - b_v for a_v, b_v in zip(a, b))

    def add(a, b):
        return tuple(a_v + b_v for a_v, b_v in zip(a, b))

    total = 0
    for id, blueprint in enumerate(blueprints, start=1):
        best_global = 0

        @lru_cache(maxsize=None)
        def dfs(resources=(0, 0, 0, 0), robots=(1, 0, 0, 0), time_left=24):
            nonlocal best_global

            if time_left == 0:
                best_global = max(best_global, resources[-1])
                return resources[-1]

            max_possible = resources[3] + robots[3] * time_left + time_left*(time_left-1)//2
            if max_possible <= best_global:
                return 0

            best = dfs(add(resources, robots), robots, time_left - 1)
            for i, r_type in enumerate(["ore_robot", "clay_robot", "obsidian_robot", "geode_robot"]):
                if can_create(resources, blueprint[r_type]):
                    new_robots = tuple(count + 1 if j == i else count for j, count in enumerate(robots))
                    best = max(
                        best,
                        dfs(
                            add(
                                subtract(resources, blueprint[r_type]),
                                robots
                            ),
                            new_robots,
                            time_left - 1,
                        )
                    )

            best_global = max(best_global, resources[-1])
            return best

        dfs()
        total += id * best_global
        print(f"{id}/{len(blueprints)}")
    print(total)


if __name__ == "__main__":
    main()
