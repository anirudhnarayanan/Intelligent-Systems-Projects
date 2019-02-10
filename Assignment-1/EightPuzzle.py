import copy

class EightPuzzle:
    def __init__(self):
        self.board = [[None for i in range(3)] for j in range(3)]
        self.correct_positions = {}
        self.blank_pos = []
 #the constructor defined here is used the state as a 3*3 number board
 #correct and blank positions are initialized
    def start_positions(self,positions):
        k = 0
        for i in range(3):
            for j in range(3):
                self.board[i][j] = positions[k]
                if positions[k] == 0:
                    self.blank_pos = [i,j]
                k+=1
    #this function defines the positions as a funnction of x,y coordinates
    #the position of the 0 is recorded and its coordinate is stored ie
    #this is for the initial state


        #self.print_board()

    def set_goal_state(self,goal_state):
        for i in range(len(goal_state)):
            self.correct_positions[goal_state[i]] = [i/3,i%3]
    #the above block is used for setting goal state and records
    #coordinates of the correct positions
    
    @staticmethod
    def printarrayboard(tempboard):
        for i in range(len(tempboard)):
            if i%3 == 0:
                print "\n"
                print tempboard[i],
            else:
                print tempboard[i],

            
        print "\n"


    def print_board(self):
        for i in range(3):
            for j in range(3):
                if not ((3*i)+j) % 3 == 0:
                    print self.board[i][j],
                else:
                    print "\n"
                    print self.board[i][j],
  #above block used for printing the states as a 3*3 board
    def current_cost(self,htype): #htype is the heuristic type 0 for manhattan, 1 for misplaced tiles
        cost = 0
        if htype == 0:
            for i in range(3):
                for j in range(3):
                    if not self.board[i][j] == 0:
                        cost += abs(i-self.correct_positions[self.board[i][j]][0]) + abs(j-self.correct_positions[self.board[i][j]][1]) 
            #cost calculation for various states by calculating the distnace betweeb a coordinate 
            #of an element in the current state and a coordinate of the element in the goal state
            #in this block the x and y coordinate differences are separately calculated and added
            #print cost 

        else:
            for i in range(3):
                for j in range(3):
                    if not self.board[i][j] == 0:
                        cost += 0 if abs(i-self.correct_positions[self.board[i][j]][0]) + abs(j-self.correct_positions[self.board[i][j]][1]) == 0 else 1 
            #cost calculation for various states by calculating the distnace betweeb a coordinate 
            #of an element in the current state and a coordinate of the element in the goal state
            #in this block the x and y coordinate differences are separately calculated and added
        
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
            up = [self.blank_pos[0] - 1, self.blank_pos[1]]
            move_options.append(self.pseudomove(up))

        if self.blank_pos[0] + 1 <= 2 :
            down = [self.blank_pos[0] + 1, self.blank_pos[1]]
            move_options.append(self.pseudomove(down))

        if self.blank_pos[1] - 1 >= 0 :
            left = [self.blank_pos[0], self.blank_pos[1] - 1]
            move_options.append(self.pseudomove(left))

        if self.blank_pos[1] + 1 <= 2 :
            right = [self.blank_pos[0], self.blank_pos[1]+1]
            move_options.append(self.pseudomove(right))
        #the above code block is to describe options of  movement of the blank pos
        #in left right up down directions

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









