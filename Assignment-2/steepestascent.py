#!/usr/bin/env python

from heuristics.heuristic import hofx
import random
from heuristics.printqueens import printqueens



def calclow(hofxmat,n):
    low = hofxmat[0][0]
    lowi,lowj = 0,0
    for i in range(n):
        for j in range(n):
            if hofxmat[i][j] < low:
                low = hofxmat[i][j]
                lowi = i
                lowj = j

    return low,lowi,lowj

def steepestascent(n):
    board = [[0 for i in range(n)] for j in range(n)]
    all_queens = []
    queenhash = {}

    for i in range(n):
        insertindex = random.randint(0,n-1)
        board[i][insertindex] = "Q"
        all_queens.append((i,insertindex))
        queenhash[i] = insertindex

    printqueens(board,all_queens,n)

    hofxmat,myhof = hofx(board,all_queens,n)
    print(hofxmat,myhof)

    low,lowi,lowj = calclow(hofxmat,n)
    print(low,lowi,lowj)
    
    while(low < myhof):
        current_j = queenhash[lowi]
        board[lowi][current_j] = 0
        board[lowi][lowj] = "Q"
        queenhash[lowi] = lowj

        print("new best score")
        print(low)
        print("current score")
        print(myhof)
        print("where my queens are now")
        print(all_queens)
        print("where i need to move them")
        print(lowi,lowj)
        print("the one i am moving")
        print(lowi,current_j)
        all_queens.remove((lowi,current_j))
        all_queens.append((lowi,lowj))

        printqueens(board,all_queens,n)
        print("\n")

        hofxmat,myhof = hofx(board,all_queens,n)
        low,lowi,lowj = calclow(hofxmat,n)
    

    print(myhof)




