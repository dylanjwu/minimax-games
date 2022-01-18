
import sys
from utils import *

class AI:

    def evaluate(self, board):

        if self.isWin(board, PLAYER):
            return -10

        elif self.isWin(board, COMP):
            return 10

        elif self.isFull(board):
            return 0

        return None

    def alpha_beta(self, game):
        board = game.getBoard()

        indices = [(i,j) for i in range(len(board)) for j in range(len(board))]

        board_copy = [a[::] for a in board]

        maxx = -sys.maxsize
        pos = ()
        for position in indices:
            board_copy = [a[::] for a in board]
            i,j=position
            if board_copy[i][j] == EMPTY:
                board_copy[i][j] = COMP 
                score = self.ab_helper(board_copy, -sys.maxsize, sys.maxsize, True, 0)
                if maxx < score:
                    maxx = score
                    pos = position
                board_copy[i][j] = EMPTY

        # self.game.markSquare(pos[0], pos[1], COMP)
        return pos

    def ab_helper(self, board, alpha, beta, is_min, depth):

        indices = [(i,j) for i in range(len(board)) for j in range(len(board))]

        if (ev := self.evaluate(board)) != None:
            return ev

        if is_min:
            res = sys.maxsize

            for position in indices:
                i, j = position

                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER
                    res = min(res, self.ab_helper(board, alpha, beta, False, depth+1))
                    board[i][j] = EMPTY

                    beta = min(res, beta)
                    if beta <= alpha:
                        break 

            return res
        else:
            res = -sys.maxsize

            for position in indices:
                i, j = position

                if board[i][j] == EMPTY:
                    board[i][j] = COMP
                    res = max(res, self.ab_helper(board, alpha, beta, True, depth+1))
                    board[i][j] = EMPTY

                    alpha = max(res, alpha)
                    if alpha >= beta:
                        break 

            return res

