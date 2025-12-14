import os
import functools

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

all_paths = {}
flows = {}

def main():
  with open(filename) as f:
    for line in f:
      line = line.strip()
      parts = line.split(' ')
      valve = parts[1]
      flow = parts[4].strip('rate=')
      flow = int(flow.strip(';'))
      paths = [path.strip(',') for path in parts[9:]]
      all_paths[valve] = paths
      flows[valve] = flow

    return dfs('AA')


@functools.lru_cache(maxsize=None)
def dfs(cur, opened=frozenset(), min_left=30):
    if min_left <= 0:
        return 0

    best = 0

    if flows[cur] > 0 and cur not in opened:
        new_opened = opened | {cur}
        best = max(best, (min_left - 1) * flows[cur] + dfs(cur, new_opened, min_left - 1))

    for adj in all_paths[cur]:
        best = max(best, dfs(adj, opened, min_left - 1))

    return best

if __name__ == "__main__":
  print(main())