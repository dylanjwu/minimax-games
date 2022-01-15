
import sys

EMPTY_BOARD = [
        ['#', '#','#'],
        ['#', '#','#'],
        ['#', '#','#']
]

class MiniMax:

    COMP = 'o'
    PLAYER = 'x'

    def __init__(self, board=EMPTY_BOARD):
        self.board = board
        self.indices = [(i,j) for i in range(len(self.board)) for j in range(len(self.board))]
    
    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            print(str(row))

    def mark_square(self, row, col, player):
        try:
            self.board[row][col] = player
            return True
        except IndexError:
            return False

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

        if self.isWin(board, self.PLAYER):
            return -10

        elif self.isWin(board, self.COMP):
            return 10

        elif self.isFull(board):
            return 0

        return None

    def alpha_beta(self):
        board_copy = [a[::] for a in self.board]
        maxx = -sys.maxsize
        pos = ()
        for position in self.indices:
            board_copy = [a[::] for a in self.board]
            i,j=position
            if board_copy[i][j] == '#':
                board_copy[i][j] = self.COMP 
                score = self.ab_helper(board_copy, -sys.maxsize, sys.maxsize, True, 1)
                if maxx < score:
                    maxx = score
                    pos = position
                board_copy[i][j] = '#'

        self.mark_square(pos[0], pos[1], self.COMP)
        return pos

    def ab_helper(self, board, alpha, beta, is_min, depth):
        ev = self.evaluate(board)
        if ev != None:
            print(ev if ev == 0 else "")
            return ev

        if is_min:
            res = sys.maxsize

            for position in self.indices:
                i, j = position

                if board[i][j] == '#':
                    board[i][j] = self.PLAYER
                    res = min(res, self.ab_helper(board, alpha, beta, False, depth+1))
                    board[i][j] = '#'

                    beta = min(res, beta)
                    if beta <= alpha:
                        break 

            return res
        else:
            res = -sys.maxsize

            for position in self.indices:
                i, j = position

                if board[i][j] == '#':
                    board[i][j] = self.COMP
                    res = max(res, self.ab_helper(board, alpha, beta, True, depth+1))
                    board[i][j] = '#'

                    alpha = max(res, alpha)
                    if alpha >= beta:
                        break 

            return res

