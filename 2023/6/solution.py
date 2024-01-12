#!/usr/bin/env python3
import sys
import numpy as np


def main(f):
    print('Advent of Code - Day 6\n')
    f_task_1 = open(f, 'r')
    f_task_2 = open(f, 'r')
    task_1(f_task_1)
    task_2(f_task_2)  

def task_1(f):
  time, dist = f.read().split('\n')
  time = list(map(int, time.split()[1:]))
  dist = list(map(int, dist.split()[1:]))
  f = lambda x, t : x*t - x**2
  sol = 1
  for _, (t, rec) in enumerate(zip(time, dist)):
     x = np.arange(t)
     sols  = np.fromiter((f(xi, t) for xi in x), x.dtype)
     sol *= len(sols[sols > rec])
  print(f'Solution 1: {sol}')
     

def task_2(f):
  time, dist = f.read().split('\n')
  t = int(time.split(':')[1:][0].replace(' ', ''))
  rec = int(dist.split(':')[1:][0].replace(' ', ''))
  f = lambda x, t : x*t - x**2
  x = np.arange(t)
  sols  = np.fromiter((f(xi, t) for xi in x), x.dtype)
  print(f'Solution 2: {len(sols[sols > rec])}')

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