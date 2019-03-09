#!/usr/bin/env python

import copy
from .queenhits import queenhits

def hofx(board,queens,n):
    hofx = [[] for i in range(n)]
    myhofx = queenhits(board,queens)
    for i in range(n):
        queenpos = board[i].index('Q')
        for j in range(n):
            if not j == queenpos or True:
                tempboard = copy.deepcopy(board)
                tempboard[i][queenpos] = 0
                tempboard[i][j] = "Q"
                temp_pos = copy.deepcopy(queens)
                temp_pos.remove((i,queenpos))
                temp_pos.append((i,j))
                hofx[i].append(queenhits(tempboard,temp_pos))    #calculate queen hits if 

    return hofx,myhofx


                

