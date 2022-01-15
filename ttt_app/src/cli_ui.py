from tictactoe import MiniMax 

is_comp = False
mm = MiniMax()

mm.print_board()
while not mm.isFull(mm.board):
    print('\n')
    if is_comp:
        ai_move = mm.alpha_beta()  
        ai_row, ai_col = ai_move
        mm.mark_square(ai_row, ai_col, mm.COMP)
        is_comp = False

        if mm.isWin(mm.board, mm.COMP):
            print("Computer wins! You lose.")
            break
    else:
        inp_row = int(input("Enter row:"))
        inp_col = int(input("Enter column:"))
        if mm.mark_square(inp_row, inp_col, mm.PLAYER):
            is_comp = True
        else:
            print("Invalid move, try again")

        print("HERE")
        if mm.isWin(mm.board, mm.PLAYER):
            print("You win!")
            break

    mm.print_board() 
# print("it's a draw!")

