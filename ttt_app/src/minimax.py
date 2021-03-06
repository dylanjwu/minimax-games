
import sys
from Game import TicTacToe
from utils import *
import Game as g

class AI:

    def __init__(self, game):
        self.game = game
        self.indices = [(i,j) for i in range(game.cols) for j in range(game.rows)]

    def evaluate(self, board):

        if self.game.isWin(board, PLAYER):
            return -10

        elif self.game.isWin(board, COMP):
            return 10

        elif self.game.isFull(board):
            return 0

        return None

    def alpha_beta(self, board):

        indices = [(i,j) for i in range(len(board)) for j in range(len(board))]

        board_copy = [a[::] for a in board]

        maxx = -sys.maxsize
        pos = (None, None)
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

        if (ev := self.evaluate(board)) != None:
            return ev

        if is_min:
            res = sys.maxsize

            for position in self.indices:
                i, j = position

                if board[i][j] == EMPTY:

                    board_copy = [a[::] for a in board]
                    board_copy[i][j] = PLAYER
                    res = min(res, self.ab_helper(board_copy, alpha, beta, False, depth+1))

                    beta = min(res, beta)
                    if beta <= alpha:
                        break 

            return res
        else:
            res = -sys.maxsize

            for position in self.indices:
                i, j = position

                if board[i][j] == EMPTY:
                    board_copy = [a[::] for a in board]
                    board_copy[i][j] = COMP
                    res = max(res, self.ab_helper(board_copy, alpha, beta, True, depth+1))

                    alpha = max(res, alpha)
                    if alpha >= beta:
                        break 

            return res

ttt = g.TicTacToe()
ai = AI(ttt)

board = [['o', '#', '#'],
         ['o', 'x', '#'],
        ['x', 'o', '#']]


print(ai.alpha_beta(board))
