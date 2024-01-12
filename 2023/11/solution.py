#!/usr/bin/env python3
import sys
import time
import numpy as np
import itertools
from bisect import bisect
from copy import deepcopy
from collections import defaultdict
from matplotlib import pyplot as plt
import networkx as nx


def main(f):
    print('Advent of Code - Day 6\n')
    f_task_1 = open(f, 'r')
    f_task_2 = open(f, 'r')
    task_1(f_task_1)
    task_2(f_task_2)  


def conv_to_graph(uni):
  #print(np.where(pipes == 'S')) 
  c = 0
  nodes = {}
  for x, line in enumerate(uni):
    for y, char in list(enumerate(line)):
        if char == '#':
          nodes[c] = (x,y)
          c += 1
  return nodes

   
def expand(uni, n = 1):
  uni_c = uni.copy()
  s = 0
  c = 1
  for i,row in enumerate(uni):
    if set(row) == {'.'}:
      for _ in range(n):
        uni_c.insert(i + s, row)
      s += n

  s = 0
  T = list(zip(*uni_c))
  T_c = T.copy()
  for j,col in enumerate(T): 
    if set(col) == {'.'}:
      for _ in range(n):
        T_c.insert(j + s, col)
      s += n
  return list(zip(*T_c))

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def task_1(f):
  uni = expand([list(itertools.chain.from_iterable(list(map(str, s.split())))) for s in f.readlines()])
  G = conv_to_graph(uni)
  distance = 0
  for star1,star2 in itertools.combinations(G.keys(), 2):
     distance += manhattan(G[star1], G[star2])
  print(f'Solution 1: {distance}')

def task_2(f):
  grid = [list(itertools.chain.from_iterable(list(map(str, s.split())))) for s in f.readlines()]
  empty_rows = [i for i,line in enumerate(grid) if '#' not in line]
  empty_columns = [x for x, col in enumerate(list(zip(*grid))) if set(col) == {'.'}]
  expand_by = 1_000_000 - 1
  galaxies = []
  for y, row in enumerate(grid):
     for x, col in enumerate(row):
        if col != '.':
           dx = expand_by * bisect(empty_columns, x)
           dy = expand_by * bisect(empty_rows, y)
           galaxies.append((x + dx, y + dy))
  dist = 0
  for a, b in itertools.combinations(galaxies, 2):
    dist += manhattan(a,b)
  print(f'Solution 2: {dist}')

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