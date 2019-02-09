#!/usr/bin/env python

from AStar import Solver
import sys

def main(input_states,goal):
    print input_states
    print goal
    a = Solver(input_states,goal)
    print a.ASTAR()

if __name__ == "__main__":
    if len(sys.argv) < 3: 
        print "Usage %s <comma separated start state> <comma separated goal state> <heuristic 0/1 -> manhattan/misplaced tiles"%sys.argv[0]
        sys.exit(-1)


    k =0
    positions = sys.argv[1].split(",")[:9]
    goal = sys.argv[2].split(",")[:9]

    positions = map(int,positions)
    goal = map(int,goal)
    input_states = [[None for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            input_states[i][j] = positions[k]

            k+=1

    main(input_states,goal)





    
        
