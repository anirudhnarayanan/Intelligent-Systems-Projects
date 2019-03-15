#!/usr/bin/env python

from heuristics.heuristic import hofx
import random
from heuristics.printqueens import printqueens
import copy





def calclow(hofxmat,n):
    low = hofxmat[0][0]
    lowi,lowj = 0,0
    lowcoords = {}
    for i in range(n):
        for j in range(n):
            if hofxmat[i][j] < low:
                low = hofxmat[i][j]
                lowi = i
                lowj = j
                lowcoords = {}
                lowcoords[(lowi,lowj)] = 0

            elif hofxmat[i][j] == low:
                lowcoords[(i,j)] = 0


    return lowcoords,low

def sidewaysascent(n,printme = False):
    board = [[0 for i in range(n)] for j in range(n)]
    all_queens = []
    queenhash = {}

    for i in range(n):
        insertindex = random.randint(0,n-1)
        board[i][insertindex] = "Q"
        all_queens.append((i,insertindex))
        queenhash[i] = insertindex

    first_board = copy.deepcopy(board)

    if printme == True:
        printqueens(board,all_queens,n)

    hofxmat,myhof = hofx(board,all_queens,n)
    #print(hofxmat,myhof)

    lowcoords,low = calclow(hofxmat,n)
    tryloc = list(lowcoords.keys())[random.randint(0,len(lowcoords.keys())-1)]
    lowi = tryloc[0]
    lowj = tryloc[1]
    #print(low,lowi,lowj)
    count = 0
    total_count = 0
    while(low <= myhof and count < 200 and myhof>0):
        current_j = queenhash[lowi]
        board[lowi][current_j] = 0
        board[lowi][lowj] = "Q"
        queenhash[lowi] = lowj

        if printme == True:
            print("new maxima")
            print(low)
            print("current maxima")
            print(myhof)
        #print("where my queens are now")
        #print(all_queens)
        #print("where i need to move them")
        #print(lowi,lowj)
        #print("the one i am moving")
        #print(lowi,current_j)
        all_queens.remove((lowi,current_j))
        all_queens.append((lowi,lowj))

        if printme == True:
            printqueens(board,all_queens,n)
            print("\n")

        hofxmat,myhof = hofx(board,all_queens,n)
        lowcoords,low = calclow(hofxmat,n)

        tryloc = list(lowcoords.keys())[random.randint(0,len(lowcoords.keys())-1)]
        lowi = tryloc[0]
        lowj = tryloc[1]
        count +=1

        if low < myhof:
            count = 0

        total_count+=1

    

    #print(myhof)
    if printme == True:
        print("current score :" + str(myhof))
        print("total count of iterations: " + str(total_count))
        
        if myhof == 0:
            print("Solution Found")
        else:
            print("Solutionn Not found")

    return myhof,total_count,first_board



if __name__ == "__main__":
    import sys
    #success=0
    sidewaysascent(8)
    #for i in range(1000):
    #    success+=1 if steepestascent(8) == 0 else 0

    #print(float(success)*100/float(1000))
