from minimax import AI
import Game as g
from utils import *

is_comp = False
game = g.TicTacToe()
ai = AI(game)

game.printBoard()
while not game.isFull(game.getBoard()):
    print('\n')
    if is_comp:
        ai_move = ai.alpha_beta(game.getBoard())  
        ai_row, ai_col = ai_move
        game.markSquare(ai_row, ai_col, COMP)
        is_comp = False

        if game.isWin(game.getBoard(), COMP):
            print("Computer wins! You lose.")
            break
    else:
        inp_row = int(input("Enter row:"))
        inp_col = int(input("Enter column:"))
        if game.markSquare(inp_row, inp_col, PLAYER):
            is_comp = True
        else:
            print("Invalid move, try again")

        print("HERE")
        if game.isWin(game.getBoard(), PLAYER):
            print("You win!")
            break

    game.printBoard() 
# print("it's a draw!")

