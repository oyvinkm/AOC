#!/usr/bin/env python3
import sys
import time
import numpy as np
import itertools 
from collections import defaultdict


def main(f):
    print('Advent of Code - Day 6\n')
    f_task_1 = open(f, 'r')
    f_task_2 = open(f, 'r')
    task_1(f_task_1)
    task_2(f_task_2)  

def get_diff_1(delta):
  deltas = [delta]
  while any(delta) != 0:
    delta = np.diff(delta)
    deltas.insert(0, list(delta))
  d = 0
  for i, delta in enumerate(deltas):
     if i < len(deltas) - 1:
      deltas[i+1].append(delta[-1] + deltas[i+1][-1])
  return deltas[-1][-1]

def get_diff_2(delta):
  deltas = [delta]
  while any(delta) != 0:
    delta = np.diff(delta)
    deltas.insert(0, list(delta))
  for i, delta in enumerate(deltas):
     if i < len(deltas) - 1:
      deltas[i+1].insert(0,deltas[i+1][0]- delta[0])
  return deltas[-1][0]
    
def task_1(f):
  seq = [list(map(int, s.split())) for s in f.readlines()]
  sol = 0
  for s in seq:
    sol += get_diff_1(s)
  print(f'Solution 1: {sol}')

def task_2(f):
  seq = [list(map(int, s.split())) for s in f.readlines()]
  sol = 0
  for s in seq:
    sol += get_diff_2(s)
  print(f'Solution 2: {sol}')

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