
import sys
board = [
    ['o', '#','#'],
    ['#', '#','#'],
    ['x', '#','o']
]

def isFull(board):
    for arr in board:
        for el in arr:
            if el == '#':
                return False
    return True

def winsDiagonal(board, player):
    left = board[0][0] == board[1][1] == board[2][2] == player
    right = board[0][2] == board[1][1] == board[2][0] == player
    return left or right

def winsColumn(board, player):
    transpose = [['' for _ in board] for _ in board]
    for i in range(len(board)):
        transpose[i] = []
        for j in range(len(board[i])):
            transpose[i].append(board[j][i])  
    return winsRow(transpose, player)

def winsRow(board, player):
    for row in board:
        if row == [player, player, player]:
            return True
    return False

def isWin(board, player):
    return winsRow(board, player) or winsColumn(board, player) or winsDiagonal(board, player)

def allBoards(board):
    win_boards = []
    draw_boards = []

    def allTTTBoards(board, isO=True):

        player = 'o' if isO else 'x'

        if isWin(board, 'o') or isWin(board, 'x'):
            win_boards.append(board)
            return 

        elif isFull(board):
            draw_boards.append(board) 
            return 

        for i in range(len(board)):
            for j in range(len(board[i])):
                boardCopy = [row[:] for row in board]
                if boardCopy[i][j] == '#':
                    boardCopy[i][j] = player
                    # print(boardCopy)
                    allTTTBoards(boardCopy, not isO)

    allTTTBoards(board, True)
    return {"wins": win_boards, "draws": draw_boards}

BOARDS = []
COMP = 'o'
PLAYER = 'x'

def evaluate(board):
    if isWin(board, PLAYER):
        BOARDS.append(board)
        return (1, board)

    elif isWin(board, COMP):
        return (-1, board)

    elif isFull(board):
        return (0, board)

    return ()



def alpha_beta(board):
    return max_value(board, (), -sys.maxsize, sys.maxsize)
    

def min_value(board, moves, alpha, beta):

    if (e := evaluate(board)) != ():
        return (e[0], e[1], moves)

    res = sys.maxsize
    final_board = []
    best_moves = ()

    for i in range(len(board)): 
        end_loop = False
        for j in range(len(board)):
            if board[i][j] == '#':
                boardCopy = [a[:] for a in board]
                boardCopy[i][j] = PLAYER
                val, b, moves = max_value(boardCopy, moves + ((i, j)), alpha, beta)                
                if val < res:
                    res = val
                    best_moves = moves
                    final_board = b

                beta = min(res, beta)

        #         if res <= alpha:
        #             end_loop = True
        #             break 
        # if end_loop:
        #     break

    return (res, final_board, best_moves)

def max_value(board, moves, alpha, beta):

    if (e := evaluate(board)) != ():
        return (e[0], e[1], moves)

    res = -sys.maxsize
    final_board = []
    best_moves = ()
    for i in range(len(board)): 
        end_loop = False
        for j in range(len(board)):
            if board[i][j] == '#':
                boardCopy = [a[:] for a in board]
                boardCopy[i][j] = COMP
                val, b, moves = min_value(boardCopy, moves + ((i, j)), alpha, beta)                
                if val > res:
                    res = val
                    final_board = b
                    best_moves = moves
                        
                alpha = max(res, alpha)

                # if res >= beta:
                #     end_loop = True
                #     break 

        # if end_loop:
        #     break

    return (res, final_board, best_moves)    

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

res = alpha_beta(boards[2])
print(res)
# print(BOARDS)
# for b in BOARDS:
#     print(str(b) + '\n')