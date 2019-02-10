#!/usr/bin/env python


from Queue import PriorityQueue
from Node import Node

class Solver:
    def __init__(self,Puzzle,Goal,htype):
        self.puzzle = Puzzle  #Board in 2d list format
        self.goal = Goal   #Goal in single list format
        self.htype = htype
        self.pq = PriorityQueue()
#constructor defined to initialize puzzle and goal and queue


    def ASTAR(self):
        depth = 0
        now_node = Node(self.puzzle,self.goal,depth,self.htype)
        self.pq.put(now_node)
        explored = []
 #intial parent node is put into the priority queue 
        steps = 0
        temp_exec = 0
        generated = 0
        while self.pq and temp_exec < 20000:
            #as long as queue as elements the child elements are popped 
            #and unexplored nodes are expanded and depth of the expanded nodes are 
            # calculated as gofx
            nextchild = self.pq.get()
            if not nextchild.myeightpuzzle.board in explored:
                depth = nextchild.gofx
                nextchild.myeightpuzzle.print_board()
                print "-------"

                manhattan_cost = nextchild.myeightpuzzle.current_cost(self.htype)
                if manhattan_cost == 0:
                    #if manhattan cost is 0 return the goal the number of steps
                    #taken to reach there and gofx ie depth at which goal is found
                    return self.goal,steps,nextchild.gofx,generated,nextchild
                depth = depth + 1
                for child in nextchild.next:
                    if not child in explored:
                        self.pq.put(Node(child,self.goal,depth,self.htype,nextchild))
                        generated +=1
                #if goal is not reached next children ie after expansion of parent 
                #are put in the queue
                temp_exec += 1
                steps = steps + 1
                explored.append(nextchild.myeightpuzzle.board)
                #the immediately above line keeps a record of explored nodes



                    
                    
            


