#!/usr/bin/env python3
import sys
import time
import numpy as np
import itertools
import regex as re
from math import lcm
from collections import defaultdict, OrderedDict

MAX_ITER = 1e10


def main(f):
    print('Advent of Code - Day 6\n')
    f_task_1 = open(f, 'r')
    f_task_2 = open(f, 'r')
    #task_1(f_task_1)
    task_2(f_task_2)  

class GNode:
  def __init__(self, args):
    self.val = args[0]
    self.l = args[1]
    self.r = args[2]
  def __repr__(self):
     return f'val : {self.val}, left : {self.l}, right : {self.r}'


class SNode:
  def __init__(self, args):
    self.val = args[0]
    self.l = args[1]
    self.r = args[2]
  def __repr__(self):
     return f'val : {self.val}, left : {self.l}, right : {self.r}'

def task_1(f):
  instructions, *nodes = f.read().split('\n\n')
  instructions = list(map(str, instructions))
  nodes = [GNode(re.findall(r'[0-9A-Z]{3}', x)) for x in nodes[0].split('\n')]
  nodes = {x.val:x for x in nodes}
  curr = nodes['AAA']
  steps = 0
  i = 0
  while steps < MAX_ITER:
    instr = instructions[i]
    match instr:
      case 'R':
        steps += 1
        curr = nodes[curr.r]
        if curr.val == 'ZZZ':
           break
      case 'L':
        steps += 1
        curr = nodes[curr.l]
        if curr.val == 'ZZZ':
           break
    if i == len(instructions) - 1:
      i = 0
    else:
      i += 1
  print(f'Solution 1 : {steps}')

def move(nodes, curr, instr):
  p = nodes[curr]
  print(p)
  for i, inst in enumerate(itertools.chain.from_iterable(itertools.repeat(instr))):
    if p.val.endswith('Z'):
      return i
    elif inst == 'R':
      p = nodes[p.r]
    else:
      p = nodes[p.l]

def task_2(f):
  instructions, *nodes = f.read().split('\n\n')
  instructions = list(map(str, instructions))
  nodes = [GNode(re.findall(r'[0-9A-Z]{3}', x)) for x in nodes[0].split('\n')]
  nodes = {x.val:x for x in nodes}
  dists = [move(nodes, curr, instructions) for curr in nodes.keys() if curr.endswith('A')]
  sol = lcm(*dists)
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