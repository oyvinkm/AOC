#!/usr/bin/env python3
import sys
import time
import numpy as np
import itertools
from collections import defaultdict, Counter


def main(f):
    print('Advent of Code - Day 6\n')
    f_task_1 = open(f, 'r')
    f_task_2 = open(f, 'r')
    task_1(f_task_1)
    task_2(f_task_2)  

""" 
- Five of a kind, where all five cards have the same label: AAAAA
- Four of a kind, where four cards have the same label and one card has a different label: AA8AA
- Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
- Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
- Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
- One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
- High card, where all cards' labels are distinct: 23456 
"""

class Hand:
  def __init__(self, hand : str, bid : int, joker = False):
    self.hand = hand
    if joker:
      try:
        most_common = Counter(hand.replace('J', '')).most_common(1)[0][0]
      except IndexError:
        most_common = 'J'
      self.tmp_hand = hand.replace('J', most_common)
    else:
      self.tmp_hand = hand
    self.set = set(hand)
    self.dict = Counter(self.tmp_hand)
    self.rank = self.calc_rank()
    self.bid = bid
  def __repr__(self):
     return f'{self.hand}'  
  def calc_rank(self):
    if 5 in self.dict.values():
      return 'five_kind'
    elif four_a_kind(self.dict):
      return 'four_kind'
    elif house(self.dict):
      return 'house'
    elif three_of_a_kind(self.dict):
      return 'three_kind'
    elif count_pairs(self.dict) > 0:
      if count_pairs(self.dict) == 2:
        return 'two_pair'
      else:
        return 'one_pair'
    else:
      return 'high_card'
    

def count_pairs(d):
  return (sum(x == 2 for x in d.values()))

def four_a_kind(d):
  return 4 in d.values()

def house(d):
  sort_d = np.sort(list(d.values()))
  return np.array_equal(sort_d, np.array([2,3]))

def three_of_a_kind(d):
  return 3 in d.values()

def high_card(d):
  if len(d.keys()) == 5:
    return max(d.keys())

card_strength = {'A':13, 'K':12, 'Q':11, 'J':0, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}
card_strength_joker = {'A':13, 
                       'K':12, 
                       'Q':11, 
                       'J':0, 
                       'T':9, 
                       '9':8, 
                       '8':7, 
                       '7':6, 
                       '6':5, 
                       '5':4, 
                       '4':3, 
                       '3':2, 
                       '2':1}

def get_card_strength(x): return card_strength[x]
def get_card_strength_joker(x): return card_strength_joker[x]

           


def task_1(f):
  buckets = {'five_kind' : [],
           'four_kind' : [],
           'house' : [],
           'three_kind' : [],
           'two_pair' : [],
           'one_pair' : [],
           'high_card' : []}

  lines = f.readlines()
  for l in lines:
    hand, bid = l.split(' ')
    hand = Hand(hand, int(bid))
    buckets[hand.rank].append(hand)
  for bucket, h in buckets.items():
    buckets[bucket] = sorted(h, key=lambda x : list(map(get_card_strength, x.hand)))
  rank = 1
  winnings = 0
  for _, hlist in reversed(buckets.items()):
    for h in hlist:
      winnings += rank * h.bid
      rank += 1
  print(f'Solution 1: {winnings}')
  

  
  #time = list(map(str, time.split()[1:]))
  #bid = int(dist.split(':')[1:][0].replace(' ', ''))

  

def task_2(f):
  buckets = {'five_kind' : [],
           'four_kind' : [],
           'house' : [],
           'three_kind' : [],
           'two_pair' : [],
           'one_pair' : [],
           'high_card' : []}

  lines = f.readlines()
  for l in lines:
    hand, bid = l.split(' ')
    hand = Hand(hand, int(bid), True)
    buckets[hand.rank].append(hand)
  for bucket, h in buckets.items():
    buckets[bucket] = sorted(h, key=lambda x : list(map(get_card_strength_joker, x.hand)))
  rank = 1
  winnings = 0
  for _, hlist in reversed(buckets.items()):
    for h in hlist:
      winnings += rank * h.bid
      print(f'Hand : {h.hand}, work hand : {h.tmp_hand} rank: {rank}, bid : {h.bid}, type : {h.rank}, count : {h.dict}')
      rank += 1
  print(f'Solution 2: {winnings}')

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