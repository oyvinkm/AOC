#!/usr/bin/env python3
import sys
import time
from collections import defaultdict


def main(f):
    print('Advent of Code - Day 6\n')
    f_task_1 = open(f, 'r')
    f_task_2 = open(f, 'r')
    task_1(f_task_1)
    task_2(f_task_2)

def read_command(commands):
  sizes = defaultdict(int)
  stack = []
  for i,c in enumerate(commands):
    if c.startswith('$ ls') or c.startswith('dir'):
      continue
    if c.startswith('$ cd'):
      dest = c.split()[2]
      if dest == '..':
        stack.pop()
      else:
          path = f"{stack[-1]}_{dest}" if stack else dest
          stack.append(path)
    else:
        size, file = c.split()
        for path in stack:
          sizes[path] += int(size)
  return sizes

def task_1(f):
    commands = f.readlines()
    sizes = read_command(commands)
    sum = 0
    for val in sorted(sizes.values()):
       if val < 100000:
          sum += val
    print(f'Solution 1 : {sum}')


def task_2(f):
    tot_space = 70000000
    needed_space = 30000000
    commands = f.readlines()
    sizes = read_command(commands)
    req_free_space = sizes['/'] - (tot_space - needed_space)
    for val in sorted(sizes.values()):
       if val > req_free_space:
          print(f'Solution 2: {val}')
          break


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 1:
       input = 'input.txt'
    else:
      match args[0]:
          case 'ex':
            input = 'example.txt'
          case _:
            input = 'input.txt'
    main(input)