import os
import numpy as np

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

ALL_SPACE = 70000000
TOTAL_SPACE = 47052440
MAX_SIZE = 100000
NECESSARY_SPACE = 30000000

def main():
  directories = {'/': {}}
  path = []
  with open(filename) as f:
    line = f.readline()
    while line:
      line = line.strip()
      args = line.split(' ')
      
      cur_dir = {}
      for path_part in path:
        if not cur_dir:
          cur_dir = directories[path_part]
        else:
          cur_dir = cur_dir[path_part]

      # User command
      if args[0] == "$":
        if args[1] == "cd":
          if (args[2]) == "..":
            path.pop()
          else:
            path.append(args[2])
        elif args[1] == "ls":
          entry = f.readline().strip()
          last_pos = f.tell()
          while not "$" in entry and entry:
            entry_args = entry.split(' ')
            if entry_args[0] == "dir":
              cur_dir[entry_args[1]] = {}
            else:
              cur_dir[entry_args[1]] = int(entry_args[0])

            last_pos = f.tell()
            entry = f.readline().strip()
          f.seek(last_pos)
    
      line = f.readline()

  return dfs1(directories, 0), dfs2(directories, [])

def dfs1(directories, small_sum):
  size = 0
  for name in directories.keys():
    if isinstance(directories[name], int):
      size += directories[name]
    else:
      subdir_size, small_sum = dfs1(directories[name], small_sum)
      size += subdir_size

  if(size < MAX_SIZE):
    small_sum += size
  
  return size, small_sum

def dfs2(directories, all_valid):
  size = 0
  for name in directories.keys():
    if isinstance(directories[name], int):
      size += directories[name]
    else:
      subdir_size, all_valid = dfs2(directories[name], all_valid)
      size += subdir_size

  if(ALL_SPACE - TOTAL_SPACE + size >= NECESSARY_SPACE and size not in all_valid):
    all_valid.append(size)
  
  return size, all_valid

if __name__ == "__main__":
  dfs1_output, dfs2_output = main()
  _, small_sum = dfs1_output
  _, all_valid = dfs2_output
  best_to_delete = min(all_valid)
  
  print(f"Sum of sizes of small directories: {small_sum}")
  print(f"Best dir to delete size: {best_to_delete}")
