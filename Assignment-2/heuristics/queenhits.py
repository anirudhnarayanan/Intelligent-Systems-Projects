#!/usr/bin/env python

def queenhits(board,all_queens): #board , and queenposition dictionary to know where queens are
    hits = []
    numhits = 0
    for i in range(len(all_queens)):
        for j in range(i+1,len(all_queens),1):
            if all_queens[i][0] == all_queens[j][0]:   #rows
                numhits+=1

            elif all_queens[i][1] == all_queens[j][1]:  #columns
                numhits+=1

            elif abs(all_queens[i][0] - all_queens[j][0]) == abs(all_queens[i][1] - all_queens[j][1]):  #diagonals
                numhits +=1

            #print(numhits,end=' ')
        #print("\n")

    return numhits



