#!/usr/bin/env python3
import sys
import numpy as np
import regex as re

def main(f):
    print('Advent of Code - Day 8\n')
    f_task_1 = open(f, 'r')
    f_task_2 = open(f, 'r')
    task_1(f_task_1)
    task_2(f_task_2)


def next_greater_right(arr):
    res = [-1 for i in arr]
    stack = []
    for i, num in enumerate(arr):
        while len(stack) > 0 and arr[stack[-1]] <= num: # <= instead of < since tree of equal height is considered "greater"
            index = stack.pop()
            res[index] = num
        stack.append(i)
    return np.array(res)

def next_greater_left(arr):
    res = [-1 for i in arr]
    stack = []
    for i, num in reversed(list(enumerate(arr))):
        while len(stack) > 0 and arr[stack[-1]] <= num: # <= instead of < since tree of equal height is considered "greater"
            index = stack.pop()
            res[index] = num
        stack.append(i)
    return np.array(res)


def task_1(f):
    #file = f.readline(f)
    l = [line.rstrip('\n') for line in f]
    forest = np.array([list(map(int, re.findall(r'\d', row))) for row in l], dtype=int)
    blocked_left = np.array([next_greater_left(row) for row in forest])
    blocked_right = np.array([next_greater_right(row) for row in forest])
    blocked_above = np.array([next_greater_left(row) for row in forest.T]).T
    blocked_below = np.array([next_greater_right(row) for row in forest.T]).T
    visible_trees = {}
    for i, row in enumerate(forest):
        for j, col in enumerate(forest[i]):
            if (blocked_left[i][j] == -1 
                or blocked_right[i][j] == -1 
                or blocked_above[i][j] == -1 
                or blocked_below[i][j] == -1
                ):
                visible_trees[f'{i},{j}'] = forest[i][j]
    print(len(visible_trees))

def next_view_right(arr):
    res = [-1 for i in arr]
    stack = []
    for i, num in enumerate(arr):
        while len(stack) > 0 and arr[stack[-1]] <= num: # <= instead of < since tree of equal height is considered "view"
            index = stack.pop()
            res[index] = i
        stack.append(i)
    return np.array(res)

def next_view_left(arr):
    res = [-1 for i in arr]
    stack = []
    for i, num in reversed(list(enumerate(arr))):
        while len(stack) > 0 and arr[stack[-1]] <= num: # <= instead of < since tree of equal height is considered "view"
            index = stack.pop()
            res[index] = i
        stack.append(i)
    return np.array(res)

def task_2(f):
     #file = f.readline(f)
    l = [line.rstrip('\n') for line in f]
    forest = np.array([list(map(int, re.findall(r'\d', row))) for row in l], dtype=int)
    blocked_left = np.array([next_greater_left(row) for row in forest])
    blocked_right = np.array([next_greater_right(row) for row in forest])
    blocked_above = np.array([next_greater_left(row) for row in forest.T]).T
    blocked_below = np.array([next_greater_right(row) for row in forest.T]).T
    visible_trees = {}
    w = len(forest[0])
    h = len(forest)
    for i, row in enumerate(forest):
        for j, col in enumerate(forest[i]):
            right_dist = blocked_right[i][j] - j if blocked_right[i][j] > 0 else w-j-i
                or blocked_right[i][j] == -1 
                or blocked_above[i][j] == -1 
                or blocked_below[i][j] == -1
                ):
                visible_trees[f'{i},{j}'] = forest[i][j]
    print(len(visible_trees))


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