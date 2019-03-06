from printqueens import printqueens
from queenhits import queenhits
from heuristic import hofx



queens = [(0,3),(1,0),(2,1),(3,2)]
board = [[0,0,0,"Q"],["Q",0,0,0],[0,"Q",0,0],[0,0,"Q",0]]
n = 4
printqueens(board,queens,n)
print(hofx(board,queens,n))
print(queenhits(board,queens))
