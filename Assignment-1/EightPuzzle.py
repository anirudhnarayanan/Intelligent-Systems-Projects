#!/usr/bin/env python
import copy

class EightPuzzle:
    def __init__(self):
        self.board = [[None for i in range(3)] for j in range(3)]
        self.correct_positions = {}
        self.blank_pos = []

    def start_positions(self,positions):
        k = 0
        
        for i in range(3):
            for j in range(3):
                self.board[i][j] = positions[k]
                if positions[k] == 0:
                    self.blank_pos = [i,j]

                k+=1



        self.print_board()

    def set_goal_state(self,goal_state):
        for i in range(len(goal_state)):
            self.correct_positions[goal_state[i]] = [i/3,i%3]


    def print_board(self):
        for i in range(3):
            for j in range(3):
                if not ((3*i)+j) % 3 == 0:
                    print self.board[i][j],
                else:
                    print "\n"
                    print self.board[i][j],

    def current_cost(self):
        cost = 0
        for i in range(3):
            for j in range(3):
                if not self.board[i][j] == 0:
                    cost += abs(i-self.correct_positions[self.board[i][j]][0]) + abs(j-self.correct_positions[self.board[i][j]][1]) 

        #print cost
        return cost
                
         
    def conv(self):
        arrayform = []
        k= 0
        for i in range(3):
            for j in range(3):
                arrayform[k] = self.board[i][j]
                k+=1

        return arrayform
                
    def options(self):
        move_options = []
        #print self.blank_pos
        if self.blank_pos[0] - 1  >= 0 :
            ##print "left called"
            left = [self.blank_pos[0] - 1, self.blank_pos[1]]
            ##print left 
            move_options.append(self.pseudomove(left))

        if self.blank_pos[0] + 1 <= 2 :
            right = [self.blank_pos[0] + 1, self.blank_pos[1]]
            move_options.append(self.pseudomove(right))

        if self.blank_pos[1] - 1 >= 0 :
            #print "up called"
            up = [self.blank_pos[0], self.blank_pos[1] - 1]
            #print up
            move_options.append(self.pseudomove(up))

        if self.blank_pos[1] + 1 <= 2 :
            down = [self.blank_pos[0], self.blank_pos[1]+1]
            move_options.append(self.pseudomove(down))
        

        return move_options

    def move(self,frm):
        self.board[self.blank_pos[0]][self.blank_pos[1]] = self.board[frm[0]][frm[1]]
        self.board[frm[0]][frm[1]] = 0
        self.blank_space = frm

        return self.conv()
    
    def pseudomove(self,frm):
        pseudoboard = copy.deepcopy(self.board)
        pseudoboard[self.blank_pos[0]][self.blank_pos[1]] = pseudoboard[frm[0]][frm[1]]
        pseudoboard[frm[0]][frm[1]] = 0
        return pseudoboard









