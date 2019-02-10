#!/usr/bin/env python

from AStar import Solver
from EightPuzzle import EightPuzzle
import sys
from compiler.ast import flatten

def main(input_states,goal,htype):
    #print input_states
    #print goal
    a = Solver(input_states,goal,htype)
    response = a.ASTAR()
    childnode = response[4]
    patharray = []
    patharray.insert(0,childnode.myeightpuzzle.board)
    while childnode.parent is not None:
        patharray.insert(0,childnode.parent.myeightpuzzle.board)
        childnode = childnode.parent


    print "\n"
    print "1) SOLUTION PATH: "
    
    for element in patharray:
        temp_el = flatten(element)
        EightPuzzle.printarrayboard(temp_el)
        print "\n"
   

    print "\n"
    print "2) GOAL: "
    EightPuzzle.printarrayboard(response[0])
    print "3) EXPANDED NODES: ",
    print response[1]
    print "\n"
    print "4) PATH DEPTH TO GOAL STATE: ",
    print response[2]
    print "\n"
    print "5) GENERATED NODES: ",
    print response[3]

if __name__ == "__main__":
    print "Usage %s <comma separated start state(in comma separated numbers)> <comma separated goal state(in comma separated numbers)> <heuristic 0/1 -> manhattan/misplaced tiles"%sys.argv[0]
    print "EXAMPLE MANHATTAN"
    print "EXAMPLE: 1,2,3,4,5,6,7,0,8 1,2,3,4,5,6,7,8,0 0"
    print "EXAMPLE MISPLACED TILES"
    print "EXAMPLE: 1,2,3,4,5,6,7,0,8 1,2,3,4,5,6,7,8,0 1"


    k =0
    arg1 = raw_input("start state: ")
    arg2 = raw_input("goal state: ")
    arg3 = raw_input("heuristic: ")
    positions = arg1.split(",")[:9]
    goal = arg2.split(",")[:9]
    htype = int(arg3)
    #print "positions argv(1)"
    positions = map(int,positions)
    goal = map(int,goal)
    input_states = [[None for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            input_states[i][j] = positions[k]

            k+=1

    main(input_states,goal,htype)




    
        
