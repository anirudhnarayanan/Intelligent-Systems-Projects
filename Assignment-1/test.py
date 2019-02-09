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
    if len(sys.argv) < 3: 
        print "Usage %s <comma separated start state> <comma separated goal state> <heuristic 0/1 -> manhattan/misplaced tiles"%sys.argv[0]
        sys.exit(-1)


    k =0
    positions = sys.argv[1].split(",")[:9]
    goal = sys.argv[2].split(",")[:9]
    htype = int(sys.argv[3])
    #print "positions argv(1)"
    positions = map(int,positions)
    goal = map(int,goal)
    input_states = [[None for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            input_states[i][j] = positions[k]

            k+=1

    main(input_states,goal,htype)




    
        
