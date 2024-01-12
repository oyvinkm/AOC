#!/usr/bin/env python3
import sys
import collections
from typing import Optional


def main(f):
    print('Advent of Code - Day 6\n')
    f_task_1 = open(f, 'r')
    f_task_2 = open(f, 'r')
    task_1(f_task_1)
    task_2(f_task_2)

def adjacent_to_symbol(row: int, start_col: int, end_col: int, schematic: list[str]) -> Optional[tuple[int, int]]:
  search_area = [(row, start_col -1), (row, end_col)]
  search_area.extend((i, col) for col in range(start_col-1, end_col+1) for i in (row-1, row+1))
  
  for r, c in search_area:
    if r < 0 or r >= len(schematic) or c < 0 or c >= len(schematic[r]):
      continue  # out of bounds check
    candidate = schematic[r][c]
    if not candidate.isnumeric() and candidate != ".":
      return r, c
  return None
    

#@register(2023, 3, 1, test=(test_engine_schematic, 4361))
""" def part_one(lines: list[str]):
  # extend schematic so we don't have to handle nums ending on right edge
  for i in range(len(lines)):
    lines[i] = lines[i] + "."
    
  part_nums = []
  for row, line in enumerate(lines):
    num = 0
    for col, char in enumerate(line):
      if char.isnumeric():
        num *= 10
        num += int(char)
        continue
      elif num == 0:
        continue
      
      col_start = col - len(str(num))
      if adjacent_to_symbol(row, col_start, col, lines) is not None:
        part_nums.append(num)
      num = 0
      
  return sum(part_nums) """


def task_1(f):
  lines = f.readlines()
  for i in range(len(lines)):
    lines[i] = lines[i] + '.'

  part_nums = []
  for row, line in enumerate(lines):
    num = 0
    for col, char in enumerate(line):
      if char.isnumeric():
        num *= 10
        num += int(char)
        continue
      elif num == 0:
        continue
      
      col_start = col - len(str(num))
      if adjacent_to_symbol(row, col_start, col, lines) is not None:
        print(num)
        part_nums.append(num)
      num = 0
      
  print(f'Solution 1: {sum(part_nums)}')
  

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