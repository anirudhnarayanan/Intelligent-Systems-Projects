#!/usr/bin/env python
from EightPuzzle import EightPuzzle

class Node:
    def __init__(self,Puzzle,Goal,gofx,htype,parent= None):
        self.myeightpuzzle = EightPuzzle()
        self.myeightpuzzle.board = Puzzle
        self.htype = htype
        self.parent = parent
        for i  in range(3):
            for j in range(3):
                if self.myeightpuzzle.board[i][j] == 0:
                    self.myeightpuzzle.blank_pos = [i,j]

        self.myeightpuzzle.set_goal_state(Goal)

        self.gofx = gofx
        self.hofx = self.myeightpuzzle.current_cost(self.htype)#path heuristic cost is calculated
        self.fofx = self.gofx + self.hofx #total cost adding depth  
        self.next = self.myeightpuzzle.options()#move options
      
        
    def setnext(self,nextstates): #Set all next values
        for i in nextstates:
            self.next.append(i)

    def getnext(self,nextstates): #Get all the options I have
        return self.next

    def __lt__(self,other):
        return self.fofx < other.fofx
    #least value of fofx is selected






        




    
    

        
