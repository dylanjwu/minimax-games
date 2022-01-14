
import sys

COMP = 'o'
PLAYER = 'x'

class MiniMax:

    def __init__(self, board):
        self.board = board #original board; should not be modified
        self.indices = [(i,j) for i in range(len(board)) for j in range(len(board))]

    def isFull(self, board):
        for arr in board:
            for el in arr:
                if el == '#':
                    return False
        return True

    def winsDiagonal(self, board, player):
        left = board[0][0] == board[1][1] == board[2][2] == player
        right = board[0][2] == board[1][1] == board[2][0] == player
        return left or right

    def winsColumn(self, board, player):
        transpose = [['' for _ in board] for _ in board]
        for i in range(len(board)):
            transpose[i] = []
            for j in range(len(board[i])):
                transpose[i].append(board[j][i])  
        return self.winsRow(transpose, player)

    def winsRow(self, board, player):
        for row in board:
            if row == [player, player, player]:
                return True
        return False

    def isWin(self, board, player):
        return (self.winsRow(board, player) or self.winsColumn(board, player) 
            or self.winsDiagonal(board, player))

    def evaluate(self, board):
        if self.isWin(board, PLAYER):
            return (-1, board)

        elif self.isWin(board, COMP):
            return (1, board)

        elif self.isFull(board):
            return (0, board)

        return ()

    def alpha_beta(self):
        return self.ab_helper(self.board, [], -sys.maxsize, sys.maxsize, False) 

    def ab_helper(self, board, moves, alpha, beta, is_min):
        if (e := self.evaluate(board)) != ():
            return (e[0], e[1], [])

        res = sys.maxsize if is_min else -sys.maxsize
        final_board, best_moves = [], []
        val = res

        for position in self.indices:
            i, j = position

            if board[i][j] != '#':
                continue

            boardCopy = [a[:] for a in board]

            if is_min:
                boardCopy[i][j] = PLAYER
                val, b, moves = self.ab_helper(boardCopy, moves[::], alpha, beta, False)                
                if val < res:
                    res = val
                    best_moves = [(i, j)] + moves
                    final_board = b

                beta = min(res, beta)

                if res <= alpha:
                    break 

            else:
                boardCopy[i][j] = COMP
                val, b, moves = self.ab_helper(boardCopy, moves[::], alpha, beta, True)                
                if val > res:
                    res = val
                    best_moves = [(i, j)] + moves
                    final_board = b

                alpha = max(res, alpha)

                if res >= beta:
                    break 

            # minimize the depth
            if val == res:
                if len(moves) < len(best_moves):
                    best_moves = [(i, j)] + moves
                    final_board = b


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

def print_board(board):
    for row in board:
        print(str(row))

def test_boards(boards):

    for i in range(len(boards)):
        print("\n\nORIGINAL BOARD: ")
        print_board(boards[i])
        MM = MiniMax(boards[i])
        res = MM.alpha_beta()
        print("Make the move: " + str(res[2][0]))
        outcome_str = "Draw!"
        if res[0] == -1:
            outcome_str = "Player (" + PLAYER +  ") wins"
        elif res[0] == 1:
            outcome_str = "Computer (" + COMP +  ") wins"
        print(f'OUTCOME: {outcome_str}')
        print(f'RESULTING BOARD:')
        print_board(res[1])

test_boards(move_2_boards)