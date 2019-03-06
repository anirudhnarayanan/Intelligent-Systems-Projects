#!/usr/bin/env python


def printqueens(board,all_queens,n):
    for i in range(n):
        for j in range(n):
            if (j,i) in all_queens:
                print(board[j][i] + " ",end='')
            else:
                print("0 ",end='')
        print("\n")
            

