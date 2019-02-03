#!/usr/bin/env python


class EightPuzzle:
    def __init__(self):
        self.board = [[None for i in range(3)] for j in range(3)]
        self.correct_positions = {1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2]}
        self.blank_pos = None

    def start_positions(self,positions):
        k = 0
        
        for i in range(3):
            for j in range(3):
                self.board[i][j] = positions[k]
                if positions[k] == 0:
                    self.blank_pos = [i,j]

                k+=1



        self.print_board()

    
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

        print cost
                

            
         


    def options(self):
        move_options = []
        if self.blank_pos[0] - 1  >= 0 :
            left = [self.blank_pos[0] - 1, self.blank_pos[1]]
            move_options.append(left)

        if self.blank_pos[0] + 1 <= 2 :
            right = [self.blank_pos[0] + 1, self.blank_pos[1]]
            move_options.append(right)

        if self.blank_pos[1] - 1 >= 0 :
            up = [self.blank_pos[0], self.blank_pos[1] - 1]
            move_options.append(up)

        if self.blank_pos[1] + 1 <= 2 :
            down = [self.blank_pos[0], self.blank_pos[1]+1]
            move_options.append(down)
        

        for i in move_options:
            print self.board[i[0]][i[1]]
        return move_options






