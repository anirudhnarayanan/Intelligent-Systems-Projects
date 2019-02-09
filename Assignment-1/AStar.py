#!/usr/bin/env python

from EightPuzzle import EightPuzzle
from Queue import PriorityQueue
from Node import Node

class Solver:
    def __init__(self,Puzzle,Goal):
        self.puzzle = Puzzle  #Board in 2d list format
        self.goal = Goal   #Goal in single list format
        self.pq = PriorityQueue()

    def ASTAR(self):
        depth = 0
        now_node = Node(self.puzzle,self.goal,depth)
        self.pq.put(now_node)
        explored = []

        steps = 0
        temp_exec = 0
        while self.pq and temp_exec < 2000:
            nextchild = self.pq.get()
            if not nextchild.myeightpuzzle.board in explored:
                depth = nextchild.gofx
                nextchild.myeightpuzzle.print_board()
                print "-------"

                manhattan_cost = nextchild.myeightpuzzle.current_cost()
                if manhattan_cost == 0:
                    return self.goal,steps,nextchild.gofx
                depth = depth + 1
                for child in nextchild.next:
                    self.pq.put(Node(child,self.goal,depth))
                
                temp_exec += 1
                steps = steps + 1
                explored.append(nextchild.myeightpuzzle.board)



                    
                    
            

