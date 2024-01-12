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

def split_list(lst, val):
    return [list(group) for k, 
            group in
            itertools.groupby(lst, lambda x: x==val) if not k]

def task_1(f):
  file = f.readlines()
  sol = 0
  for i in range(len(file)):
    tmp = split_list(file[i].split(':')[1].split(), '|')
    win, own = set(list(map(int, tmp[0]))), set(list(map(int, tmp[1])))
    num = win & own
    sol += 2**(len(num) - 1) if len(num) > 0 else 0
  print(f'Solution 1 : {sol}')

  



def task_2(f):
  file = f.readlines()
  n = np.ones(len(file), dtype = int)
  i = 0
  while i < len(file):
    tmp = split_list(file[i].split(':')[1].split(), '|')
    win, own = set(list(map(int, tmp[0]))), set(list(map(int, tmp[1])))
    length = np.arange(i+1, i+len(win & own)+1)
    for j in length:
       n[j] += 1 * n[i]
    i += 1
  print(f'Solution 2: {np.sum(n)}')

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