
import numpy as np
import itertools
from itertools import groupby
from string import ascii_letters
from collections import OrderedDict

def split_new_line(file = 'input.txt'):
  with open(file, 'r') as f:
    l = [line.rstrip('\n') for line in f]
  return l
def split_new_line_and_string(file = 'input.txt', delimiter = ''):
  with open(file, 'r') as f:
    l = [str.split(line.rstrip('\n'), delimiter) for line in f]
  return l

def split_empy_line(file = 'input.txt'):
  with open(file, 'r') as f:
    l = [list(g) for k, g in groupby(map(str.strip, f), key=lambda line: line != '') if k]
  return l

def char_to_num(char):
  return ascii_letters.index(char) +1