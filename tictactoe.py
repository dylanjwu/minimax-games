

board = [
    ['#', '#','#'],
    ['#', '#','#'],
    ['#', '#','#']
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

res = allBoards(board)
print('wins', len(res['wins']))
# for a in res['wins']
#     print(str(a) + '\n')
print('draws', len(res['draws']))
