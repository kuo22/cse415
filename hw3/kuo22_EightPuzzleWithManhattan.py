''' kuo22_AStar.py
By Kuo Hong
CSE 415 Assignment 3

The implementation for Manahttan distance heuristic.
Sums the distance for each number tiles in the puzzle.
'''
from EightPuzzle import *

# For every tile that's not blank, get the Manhattan distance
# and add to total h
def h(s):
    h = 0
    for i in range(3):
        for j in range(3):
            if s.b[i][j] != 0:
                num = s.b[i][j]
                goal_row = int (num / 3)
                goal_col = num % 3
                dist = abs(i - goal_row) + abs(j - goal_col)
                h += dist
    return h
