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
  pass

def task_2(f):
  pass

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