#!/usr/bin/env python

from heuristics.heuristic import hofx
import random
from heuristics.printqueens import printqueens
import copy
import pdb



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


    return low,lowi,lowj,lowcoords

def sidewaysascent(n):
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

    low,lowi,lowj,lowcoords = calclow(hofxmat,n)
    print(low,lowi,lowj)

    visited_boards = []
    visited_boards.append(board)
    mylowcoords = copy.deepcopy(lowcoords)

    count = 0
    
    while(low <= myhof and low > 0 and 0 in mylowcoords.values() and count < 300):
        #pdb.set_trace()
            

        tempboard = copy.deepcopy(board)
        current_j = queenhash[lowi]
        tempboard[lowi][current_j] = 0
        tempboard[lowi][lowj] = "Q"
        if not mylowcoords[(lowi,lowj)] == 1:
            mylowcoords[(lowi,lowj)] = 1
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
            board = tempboard

            printqueens(tempboard,all_queens,n)
            count +=1
            print("\n")

        else:
            lowi,lowj = [k for k,v in mylowcoords.items() if v == 0][0]

        hofxmat,myhof = hofx(tempboard,all_queens,n)
        low,newlowi,newlowj,lowcoords = calclow(hofxmat,n)

        #if not 0 in mylowcoords.values():
        #    break

        print("lowcoords")
        print(lowcoords)
        print("low")
        print(low)
        print("myhof")
        print(myhof)
    

        if low < myhof:
            mylowcoords = copy.deepcopy(lowcoords)
            lowi = newlowi
            lowj = newlowj

            print("mylow")
            print(mylowcoords)

        else:
            lowcoords.update(mylowcoords)
            mylowcoords = copy.deepcopy(lowcoords)

        
        #if not 0 in mylowcoords.values():
        #    break

        print("mylow")
        print(low)
        print(mylowcoords)


    

    print(low)
    tempboard = copy.deepcopy(board)
    current_j = queenhash[lowi]
    tempboard[lowi][current_j] = 0
    tempboard[lowi][lowj] = "Q"
    if not mylowcoords[(lowi,lowj)] == 1:
        mylowcoords[(lowi,lowj)] = 1
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
        board = tempboard

        printqueens(tempboard,all_queens,n)
        print("\n")
        print(low)
    
    return low








if __name__ == "__main__":
    answer = 0
    for i in range(300):
        print("I AM RUNNING " + str(i))
        answer+=1 if sidewaysascent(8) == 0 else 0

    sidewaysascent(8)

    print((float(answer)/float(300))*100)

