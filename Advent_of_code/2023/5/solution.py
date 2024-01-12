#!/usr/bin/env python3
import sys
import time
import numpy as np
import itertools
from collections import defaultdict, OrderedDict


def main(f):
    print('Advent of Code - Day 6\n')
    f_task_1 = open(f, 'r')
    f_task_2 = open(f, 'r')
    task_1(f_task_1)
    task_2(f_task_2)  

# = OrderedDict()
class Range:
  def __init__(self, lower, upper):
    self.lower = lower
    self.upper = upper
  def __repr__(self):
    return f'[{self.lower}, {self.upper})'
  def intersection(self, other):
     tmp = Range(max(self.lower, other.lower), min(self.upper, other.upper))
     return tmp if tmp.lower < tmp.upper else None
  def subtract(self, other):
    ins = self.intersection(other)
    if ins is None:
      return [Range(self.lower, self.upper)]
    elif (ins.lower, ins.upper) == (self.lower, self.upper):
      return []
    elif ins.lower == self.lower:
      return [Range(ins.upper, self.upper)]
    else:
      return [Range(self.lower, ins.lower), Range(ins.upper, self.upper)]
  def add(self, offset):
    return Range(self.lower + offset, self.upper + offset)
     

class Map:
  def __init__(self, map_str):
    self.rules = []
    for l in map_str.splitlines()[1:]:
        dest, source, size = map(int, l.split())
        self.rules.append((dest, source ,size))

  def convert(self, inp):
    for dest, source, size in self.rules:
       if source <= inp < source + size:
          return dest + inp - source
    return inp

def getLocation(seed, maps):
  for m in maps: 
    seed = m.convert(seed)
  return seed
    
      
  

def task_1(f):
  seeds, *map_str = f.read().split('\n\n')
  seeds = list(map(int, seeds.split()[1:]))
  maps = [Map(m_str) for m_str in map_str]
  locations = [getLocation(seed, maps) for seed in seeds]
  print(f'Solution 1: {min(locations)}')


class Task2Solver:
  def __init__(self, maps):
    self.maps = maps
    self.answer = float('inf')
  def propogate(self, r : Range, layer : int):
    if layer == len(self.maps):
      self.answer = min(self.answer, r.lower)
      return
    for dest, src, size in self.maps[layer].rules:
      map_r = Range(src, src + size)
      ins = r.intersection(map_r)
      if ins is not None:
        self.propogate(ins.add(dest - src), layer +1)
        sub = r.subtract(map_r)
        if len(sub) == 0:
          return
        r = sub[0]
        if len(sub) == 2:
          self.propogate(sub[1], layer)
    self.propogate(r, layer + 1)


def task_2(f):
  seeds, *map_str = f.read().split('\n\n')
  seeds = list(map(int, seeds.split()[1:]))
  maps = [Map(m_str) for m_str in map_str]
  solver = Task2Solver(maps)
  for i in range(0, len(seeds), 2):
    solver.propogate(Range(seeds[i], seeds[i] + seeds[i+1]), 0)
  print(f'Solution 2: {solver.answer}')

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