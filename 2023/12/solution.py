#!/usr/bin/env python3
import sys
import unittest
from loguru import logger
from functools import cache


def main(f):
    logger.success('Advent of Code - Day 12\n')
    f_task_1 = open(f, 'r')
    f_task_2 = open(f, 'r')
    task_1(f_task_1)
    task_2(f_task_2)

def make_tuple_2(line):
  record, grps = line.split(' ') 
  return '?'.join([record] * 5) + '.', tuple(map(int, grps.split(','))) * 5

def make_tuple(line):
  record, grps = line.split(' ') 
  return record, tuple(map(int, grps.split(',')))

@cache
def count_arrangements(records : tuple, grps : tuple[int, ...]) -> int:
  if not grps:
    if all(rec in ['.', '?'] for rec in records):
      return 1
    return 0
  size_frst_grp = grps[0] 
  remaining_grps = grps[1:]
  remaining_rec_spaces = sum(remaining_grps) + len(remaining_grps)
  count = 0
  for i in range(len(records) - remaining_rec_spaces - size_frst_grp + 1):
     possible_recs = '.' * i + '#' * size_frst_grp + '.'
     if all(
        rec == possible_recs or rec == '?'
        for rec, possible_recs in zip(records, possible_recs)
     ):
        count += count_arrangements(records[len(possible_recs) : ], remaining_grps)

  return count

def task_1(f):
  f = f.readlines()

  logger.success(f'Solution 1: {sum([count_arrangements(*make_tuple(l)) for l in f])}')
  

def task_2(f):
  f = f.readlines()

  logger.success(f'Solution 2: {sum([count_arrangements(*make_tuple_2(l)) for l in f])}')



class TestMakeTuple(unittest.TestCase):
    def test_make_tuple(self):
      self.assertEqual(make_tuple('???.### 1,1,3'), ('???.###', (1,1,3)))
    def test_make_tuple2(self):
      self.assertEqual(make_tuple('.??..??...?##. 1,1,3'), ('.??..??...?##.', (1,1,3)))

class TestMakeArrangement(unittest.TestCase):
  def test_arrange(self):
    self.assertEqual(count_arrangements('???.###', (1,1,3)), 1)
  def test_arrange2(self):
    self.assertEqual(count_arrangements('?###????????', (3,2,1)), 10)

class Test_Tuple_To_Arrangement(unittest.TestCase):
  def test_tuple_to_arrange(self):
    rec, grp = make_tuple('???.### 1,1,3')
    self.assertEqual(count_arrangements(rec, grp), 1)
  def test_tuple_to_arrange2(self):
    rec, grp = make_tuple('?###???????? 3,2,1')
    self.assertEqual(count_arrangements(rec,grp), 10)

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