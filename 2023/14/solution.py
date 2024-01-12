#!/usr/bin/env python3
import sys
import time
import numpy as np
import itertools
from collections import defaultdict
from pathlib import Path
from functools import cache


def main(f):
    print('Advent of Code - Day 6\n')
    f_task_1 = open(f, 'r')
    f_task_2 = open(f, 'r')
    task_1(f_task_1)
    task_2(f_task_2)  

# Original
#   O....#....
#   O.OO#....#
#   .....##...
#   OO.#O....O
#   .O.....O#.
#   O.#..O.#.#
#   ..O..#O..O
#   .......O..
#   #....###..
#   #OO..#....


def fill_line(line, load):
  split = np.split(line, np.where(line == '#')[0],)
  l = 0
  for s in split:
    length = len(s)
    s = np.delete(s, np.where(s == '.')[0])
    if not np.array_equal(s, ['#']):
      load[np.where(s == 'O')[0] + l] += 1
    l += length


def move(mat, order):
  edg = np.where(np.diff(np.hstack(([False], (mat == 0) | (mat == 1), [False]))))[0]
  edg = np.where(np.diff(np.hstack(([False], (mat == 0) | (mat == 1), [False]))))[0]
  for i in range(0, len(edg), 2):
    mat[edg[i] : edg[i + 1]] = np.sort(mat[edg[i] : edg[i + 1]])[::order]
    
#North, West, South, East
def rotate(mat):
  # north
  for column in range(mat.shape[1]):
      move(mat[:, column], order=-1)

  # west
  for row in range(mat.shape[0]):
      move(mat[row, :], order=-1)

  # south
  for column in range(mat.shape[1]):
      move(mat[:, column], order=1)

  # east
  for row in range(mat.shape[0]):
      move(mat[row, :], order=1)
 
     
      


def task_1(f):
  array = np.array([[char for char in line.strip()] for line in f.read().split('\n')]).T
  load = np.zeros(len(array[0]))
  for line in array:
    fill_line(line, load) 
  sol = sum((idx+1) * val for idx, val in enumerate(reversed(load)))
  print(f'Solution 1: {sol}') 

def printmat(mat, stri):
   map = {-1 : '#', 0 : '.', 1: 'O'}
   print(stri)
   for l in np.vectorize(map.get)(mat):
      print("".join(l))

def weight(mat):
    xx = (np.arange(mat.shape[0]) + 1)[::-1]
    cmat = np.multiply(mat.copy(), xx[:, np.newaxis])
    cmat[cmat < 0] = 0
    return cmat.sum()
   
def task_2(f):
  lines = f.read().splitlines()
  map = {"#": -1, ".": 0, "O": 1}
  mat = np.array([[map[x] for x in line] for line in lines])
  res = []
  res.append(mat.copy())
  period = (0, 0, 0)
  for i in range(1, 10000000):
    rotate(mat)
    period = (0, 0, 0)
    for n, origmat in enumerate(res, start=1):
        if np.all(mat == origmat):
            period = (i - n + 1, n, i)
            break
    if period[0] > 0:
        break
    res.append(mat.copy())
  print(period)
  residum = (1_000_000_000 - period[2]) % period[0]
  print(f"{residum=}")
  for i in range(residum):
    rotate(mat)
  print("part 2=", weight(mat))
  #load = sum((idx+1) * val for idx, val in enumerate(reversed((mat == 1).sum(axis=1))))
  #print(load)


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