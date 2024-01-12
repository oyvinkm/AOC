#!/usr/bin/env python3
import sys
import collections
import regex as re
from typing import Optional


def main(f):
    print('Advent of Code - Day 6\n')
    f_task_1 = open(f, 'r')
    f_task_2 = open(f, 'r')
    task_1(f_task_1)
    task_2(f_task_2)

    




def task_1(f):
  g = f.readlines()
  sol = 0
  for x in range(len(g)):
      for match in re.finditer('\d+', g[x]):
          try:
              for y in range(*match.span()):
                  for i in range(-1, 2):
                      for j in range(-1, 2):
                          assert not (0 <= x+i < len(g) and 0 <= y+j < len(g) and not g[x+i][y+j].isdigit() and g[x+i][y+j] != '.')
          except: sol += int(match.group())
  print(f'Solution 1 : {sol}')
  
  

def task_2(f):
  g = f.readlines()
  sol = 0
  adj = [[[] for x in range(len(g))] for x in range(len(g))]
  for x in range(len(g)):
      for match in re.finditer('\d+', g[x]):
          for y in range(*match.span()):
              for i in range(-1, 2):
                  for j in range(-1 if y == match.span()[0] else 0, 1 if y < match.span()[1]-1 else 2):
                      if 0 <= x+i < len(g) and 0 <= y+j < len(g) and g[x+i][y+j] == '*':
                          adj[x+i][y+j].append(int(match.group()))
  print(f'Solution 2: {sum(adj[x][y][0]*adj[x][y][1] for x in range(len(g)) for y in range(len(g)) if len(adj[x][y]) == 2)}')


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