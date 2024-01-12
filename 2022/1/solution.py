import numpy as np
import itertools
from itertools import groupby

with open('input.txt', 'r') as f:
  l = [np.sum(np.array(list(g), dtype = int)) for k, g in groupby(map(str.strip, f), key=lambda line: line != '') if k]

sort = np.sort(l)
print(sort)
print(sort[-3:])
print(np.sum(sort[-3:]))

#print(np.max(l))
