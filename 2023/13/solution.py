#!/usr/bin/env python3
import sys
import time
import numpy as np
import itertools
import unittest
from collections import defaultdict


def main(f):
    print('Advent of Code - Day 6\n')
    f_task_1 = open(f, 'r')
    f_task_2 = open(f, 'r')
    task_1(f_task_1)
    task_2(f_task_2)

def find_mirror(arr):
  test = lambda a,b : (a == b[::-1]).all()
  for i in range(1, len(arr)):
     l = min(len(arr) -i, i)
     if test(arr[i - l : i], arr[i : i + l]):
        return i
  return None



def find_smudge(arr):
  test = lambda a,b : (a != b[::-1]).sum() == 1
  for i in range(1, len(arr)):
     l = min(len(arr) -i, i)
     if test(arr[i - l : i], arr[i : i + l]):
        return i
  return None

def task_1(f):
  l = [
     np.array([[char for char in line.strip()] for line in arr.split('\n')]) 
     for arr in f.read().split('\n\n')
     ]
  sol = sum(
     y * 100 if (y:= find_mirror(arr)) is not None
     else find_mirror(np.rot90(arr, -1))
     for arr in l
  )
  print(f'Solution 1: {sol}')
     
  

def task_2(f):
  l = [
     np.array([[char for char in line.strip()] for line in arr.split('\n')]) 
     for arr in f.read().split('\n\n')
     ]
  anw = sum(
     y * 100 if (y:= find_smudge(arr)) is not None
     else find_smudge(np.rot90(arr, -1))
     for arr in l
  )
  print(f'Solution 2: {anw}')


class TestFindMirror(unittest.TestCase):
   def test_mirror1(self):
      self.assertEqual(find_mirror(np.array(['#','#', '#', '#', '#', '.', '#', '#', '.']), 
                                   np.array(['#','#', '#', '#', '#', '.', '#', '#', '.'])), True)
#   def test_mirror2(self):
#      self.assertEqual(find_mirror(['#','#', '#', '#', '#', '.', '#', '#', '.'], '#####.##.'), True)

if __name__ == "__main__":
    #unittest.main()
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