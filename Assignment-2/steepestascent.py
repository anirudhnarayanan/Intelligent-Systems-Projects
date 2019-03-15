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

def steepestascent(n,printme = True):
    board = [[0 for i in range(n)] for j in range(n)]
    all_queens = []
    queenhash = {}

    for i in range(n):
        insertindex = random.randint(0,n-1)
        board[i][insertindex] = "Q"
        all_queens.append((i,insertindex))
        queenhash[i] = insertindex

    
    if printme:
        printqueens(board,all_queens,n)

    hofxmat,myhof = hofx(board,all_queens,n)
    #print(hofxmat,myhof)

    low,lowi,lowj = calclow(hofxmat,n)
    #print(low,lowi,lowj)

    total_count = 0
    
    while(low < myhof):
        current_j = queenhash[lowi]
        board[lowi][current_j] = 0
        board[lowi][lowj] = "Q"
        queenhash[lowi] = lowj
        if printme == True:
            print("new maxima")
            print(low)
            print("current maxima")
            print(myhof)
        all_queens.remove((lowi,current_j))
        all_queens.append((lowi,lowj))
        if printme == True:
            printqueens(board,all_queens,n)
            print("\n")

        hofxmat,myhof = hofx(board,all_queens,n)
        low,lowi,lowj = calclow(hofxmat,n)
        total_count += 1
    
    if printme == True:
        print("Current Heuristic value: " + str(myhof))
        print("Total number of iterations: " + str(total_count))
        if myhof == 0:
            print("Solution Found")
        else:
            print("No Solution Found")
    return myhof,total_count


if __name__ == "__main__":
    answer = 0
    steepestascent(8)
    

