import os
from collections import deque
import functools

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

all_paths = {}
flows = {}

with open(filename) as f:
    for line in f:
        line = line.strip()
        parts = line.split(' ')
        valve = parts[1]
        flow = int(parts[4].split('=')[1].strip(';'))
        paths = [p.strip(',') for p in parts[9:]]
        all_paths[valve] = paths
        flows[valve] = flow

valves_with_flow = [v for v in flows if flows[v] > 0]
valve_index = {v: i for i, v in enumerate(valves_with_flow)}
all_opened_mask = (1 << len(valves_with_flow)) - 1

shortest = {}
for v in all_paths:
    q = deque([(v, 0)])
    visited = {v}
    d = {}
    while q:
        u, dist = q.popleft()
        d[u] = dist
        for nei in all_paths[u]:
            if nei not in visited:
                visited.add(nei)
                q.append((nei, dist + 1))
    shortest[v] = d


@functools.lru_cache(maxsize=None)
def dfs(pos1, pos2, opened_mask, time1, time2):
    best = 0

    for v in valves_with_flow:
        bit = 1 << valve_index[v]
        if opened_mask & bit:
            continue

        t1 = shortest[pos1][v] + 1
        if t1 <= time1:
            best = max(best,
                (time1 - t1) * flows[v] +
                dfs(v, pos2, opened_mask | bit, time1 - t1, time2)
            )

        t2 = shortest[pos2][v] + 1
        if t2 <= time2:
            best = max(best,
                (time2 - t2) * flows[v] +
                dfs(pos1, v, opened_mask | bit, time1, time2 - t2)
            )

    return best


if __name__ == "__main__":
    print(dfs('AA', 'AA', 0, 26, 26))
