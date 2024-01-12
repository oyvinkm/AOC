#!/usr/bin/env python3
import sys
import time
import numpy as np
import itertools 
from collections import defaultdict
import networkx as nx
from matplotlib import pyplot as plt


def main(f):
    print('Advent of Code - Day 6\n')
    f_task_1 = open(f, 'r')
    f_task_2 = open(f, 'r')
    task_1(f_task_1)
    task_2(f_task_2)






def task_1(f):
  data = [list(itertools.chain.from_iterable(list(map(str, s.split())))) for s in f.readlines()]

  N,M = len(data), len(data[0])
  G = nx.Graph()
  #print(np.where(pipes == 'S')) 
  for x, line in enumerate(data):
    for y, char in list(enumerate(line)):
        # North neighbour
        if x > 0 and data[x-1][y] in "|7FS" and char in "|LJS":
            G.add_edge((x, y), (x-1, y))
        # East neighbour
        if y < M-1 and data[x][y+1] in "-J7S" and char in "-LFS":
            G.add_edge((x, y), (x, y+1))
        if char == "S":
            start = (x, y)
  cycle = nx.find_cycle(G, start) 
  print(f'Solution 1 : {len(cycle) // 2}')



def task_2(f):
  data = [list(itertools.chain.from_iterable(list(map(str, s.split())))) for s in f.readlines()]

  N,M = len(data), len(data[0])
  G = nx.Graph()
  #print(np.where(pipes == 'S')) 
  for x, line in enumerate(data):
    for y, char in list(enumerate(line)):
        # North neighbour
        if x > 0 and data[x-1][y] in "|7FS" and char in "|LJS":
            G.add_edge((x, y), (x-1, y))
        # East neighbour
        if y < M-1 and data[x][y+1] in "-J7S" and char in "-LFS":
            G.add_edge((x, y), (x, y+1))
        if char == "S":
            start = (x, y)
  cycle = nx.find_cycle(G, start) 
  path_nodes = set(p[0] for p in cycle)
  seen = set()
  G2 = nx.grid_graph((N, M))
  G2.remove_nodes_from(path_nodes)
  for (x, y), (i, j) in cycle:
    # add nodes that are to the right side of a path
    dx, dy = i-x, j-y
    for i in (0, 1):
        node = x + i*dx - dy, y + i*dy + dx
        if node not in seen and node not in path_nodes:
            seen |= nx.node_connected_component(G2, node) # s1 |= s2 <-> s1 = s1 | s2
  print(f'Solution 2: {len(seen)}')




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