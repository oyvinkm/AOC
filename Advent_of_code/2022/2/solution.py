import numpy as np
import itertools
from itertools import groupby

with open('input.txt', 'r') as f:
  l = [str.split(line.rstrip('\n')) for line in f]

# X = Rock, Y = Paper, Z = Scissor
# A = Rock, B = Paper, C = Scissor
dict = {'X' : 1, 'Y' : 2, 'Z' : 3}

win = 6
draw = 3
loss = 0

""" A Y
B X
C Z """
example = [['A', 'Y'], ['B', 'X'], ['C', 'Z']]

def outcome(p1, p2): 
  p1 = p1
  p2 = p2
  if p1 == 'A':
    if p2 == 'X':
      return draw + dict['X']
    elif p2 == 'Y':
      return win + dict['Y']
    elif p2 == 'Z':
      return loss + dict['Z']
  elif p1 == 'B':
      if p2 == 'X':
        return loss + dict['X']
      if p2 == 'Y':
        return draw + dict['Y']
      if p2 == 'Z':
        return win + dict['Z']
  elif p1 == 'C':
      if p2 == 'X':
        return win + dict['X']
      elif p2 == 'Y':
        return loss + dict['Y']
      elif p2 == 'Z':
        return draw + dict['Z']
  else:
    return 0
  

def call_draw(p1):
  match p1:
    case 'A':
      return 'X'
    case 'B':
      return 'Y'
    case 'C':
      return 'Z'
def call_win(p1):
  match p1:
    case 'A':
      return 'Y'
    case 'B':
      return 'Z'
    case 'C':
      return 'X'
def call_loose(p1):
  match p1:
    case 'A':
      return 'Z'
    case 'B':
      return 'X'
    case 'C':
      return 'Y'


#X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
def strategy(p1, p2):
  match p2:
    case 'X':
      play = call_loose(p1)
      return outcome(p1, play)
    case 'Y':
      play = call_draw(p1)
      return outcome(p1, play)
    case 'Z':
      play = call_win(p1)
      return outcome(p1, play)
    case _:
      print('No Match')



sum = 0
for m in l:
  p1, p2 = m[0], m[1]
  out = strategy(p1, p2)
  sum += out
print(sum)
#print(np.max(l))
