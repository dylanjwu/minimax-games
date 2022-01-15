from tictactoe import MiniMax

boards = [
    [
        ['#', '#','#'],
        ['#', '#','#'],
        ['#', '#','#']
    ],
    [
        ['o', '#','#'],
        ['#', '#','#'],
        ['x', '#','o']
    ],
    [
        ['#', '#','x'],
        ['o', '#','#'],
        ['o', '#','#']
    ],
    [
        ['x', '#','#'],
        ['#', '#','#'],
        ['x', '#','x']
    ],
]

def create_move_2_test_boards():
    move_2_boards = []
    board_template = [['#']*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            new_board = [arr[::] for arr in board_template]
            new_board[i][j] = 'x'
            curr = (i, j)
            for k in range(3):
                for l in range(3):
                    if (k, l) != curr:
                        new_1_board = [arr[::] for arr in new_board]
                        new_1_board[k][l] = 'x'
                        if not new_board in move_2_boards:
                            move_2_boards.append(new_1_board)
    return move_2_boards

def print_board(board):
    for row in board:
        print(str(row))

def test_boards(boards):

    for i in range(len(boards)):
        print("\n\nORIGINAL BOARD: ")
        print_board(boards[i])
        MM = MiniMax()
        res = MM.alpha_beta()
        print("Make the move: " + str(res[2][0]))
        outcome_str = "Draw!"
        if res[0] == -1:
            outcome_str = "Player (" + MM.PLAYER +  ") wins"
        elif res[0] == 1:
            outcome_str = "Computer (" + MM.COMP +  ") wins"
        print(f'OUTCOME: {outcome_str}')
        print(f'RESULTING BOARD:')
        print_board(res[1])

# # test_boards(move_2_boards)
board = [['#', 'x', '#'],
        ['#', 'x', '#'],
        ['o', '#', 'o']]

mm=MiniMax(board)

res = mm.alpha_beta()
# res = mm.ab_helper(board, -sys.maxsize, sys.maxsize, True, 0)
print(res)

# print(res[2])
# for row in res[1]:
#     print(str(row))


# boards = create_move_2_test_boards()
# test_boards(boards)