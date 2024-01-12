#!/usr/bin/env python3

def main():
    print('Advent of Code - Day 6\n')
    f_task_1 = open('input.txt', 'r')
    f_task_2 = open('input.txt', 'r')
    task_1(f_task_1)
    task_2(f_task_2)


def task_1(file):
    file_content = file.read()
    idx = 0
    n = 4
    while len(set(file_content[idx:idx +n])) != n:
        idx += 1
    print(f'Solution Task 1: {idx + n}')

def task_2(file):
    file_content = file.read()
    idx = 0
    n = 14
    while len(set(file_content[idx:idx +n])) != n:
        idx += 1
    print(f'Solution Task 2: {idx + n}')


if __name__ == "__main__":
    main()