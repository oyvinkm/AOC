import numpy as np
import itertools
from itertools import groupby




def split_new_line(file = 'input.txt'):
  with open(file, 'r') as f:
    l = [str.split(line.rstrip('\n')) for line in f]
    return l

def split_empy_line(file = 'input.txt'):
  with open(file, 'r') as f:
    l = [np.sum(np.array(list(g), dtype = int)) for k, g in groupby(map(str.strip, f), key=lambda line: line != '') if k]
    return l

with open('input.txt', 'r') as f:
    l = [line.rstrip('\n') for line in f]
  
print(l[:5])