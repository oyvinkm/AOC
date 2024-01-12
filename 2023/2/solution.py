#!/usr/bin/env python3
import sys
import regex as re

def main(f):
    #print('Advent of Code - Day 6\n')
    f_task_1 = open(f, 'r')
    f_task_2 = open(f, 'r')
    task_1(f_task_1)
    task_2(f_task_2)

def eval_count(dict, r = 12, b = 13, g = 14):
   if dict['red'] > r or dict['blue'] > b or dict['green'] > g:
      return False
   else:
      return True

def task_1(f):
    limit = {'red': 12, 'green': 13, 'blue': 14}
    file = [line.rstrip('\n') for line in f]
    sol = 0
    for i,line in enumerate(file):
      _, game = line.split(': ')
      game = game.split('; ')
      impossible = False
      for g in game:
        col_val = {'red' : 0, 'green' : 0, 'blue' : 0}
        round = [rs.split(', ') for rs in g.split('; ')][0]
        for r in round:
          val, colour = r.split(' ')
          if int(val) > limit[colour]:
             impossible = True
      if not impossible:
          print(i)
          sol += i+1
    print(f'Solution 1 : {sol}')

def task_2(f):
    file = [line.rstrip('\n') for line in f]
    sol = 0
    for i,line in enumerate(file):
      _, game = line.split(': ')
      game = game.split('; ')
      min_possible = {'red' : 0, 'green' : 0, 'blue' : 0}
      for g in game:
        round = [rs.split(', ') for rs in g.split('; ')][0]
        for r in round:
          val, colour = r.split(' ')
          min_possible[colour] = max(min_possible[colour], int(val))
      power = 1
      for v in min_possible.values():
         print(v)
         power *= v
      sol += power
    print(f'Solution 2 : {sol}')


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