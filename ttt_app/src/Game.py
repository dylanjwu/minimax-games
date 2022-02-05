from utils import *
# from minimax import AI

class Game:
    def __init__(self, rows, cols, to_win):
        self.board = [[EMPTY]*cols for _ in range(rows)]
        self.to_win = to_win
        self.rows = rows
        self.cols = cols

    def clear(self):
        self.board = [[EMPTY]*self.cols for _ in range(self.rows)]

    def printBoard(self):
        for row in self.board:
            print(row)

    def getBoard(self):
        return self.board

    def markSquare(self, row, col, player):
        try:
            self.board[row][col] = player
            return True
        except IndexError:
            return False

    def isFull(self, board):
        for arr in board:
            for el in arr:
                if el == EMPTY:
                    return False
        return True

    def winsDiagonal(self, board, player):

        for row in range(len(board)):
            for col in range(len(board[0])):
                #check right
                i = row; j = col;
                player_count = 0
                while i < len(board) and j < len(board[0]):
                    if board[i][j] == player:
                        player_count += 1
                        if player_count == self.to_win:
                            return True
                    else:
                        player_count = 0
                    i+=1
                    j+=1

                #check left
                i = row; j = col;
                player_count = 0
                while i < len(board) and j >= 0:
                    if board[i][j] == player:
                        player_count += 1
                        if player_count == self.to_win:
                            return True
                    else:
                        player_count = 0
                    i+=1
                    j-=1

        return False    


    def winsColumn(self, board, player):
        transpose = [['' for _ in board] for _ in board]
        for i in range(len(board)):
            transpose[i] = []
            for j in range(len(board[i])):
                transpose[i].append(board[j][i])  
        return self.winsRow(transpose, player)

    def winsRow(self, board, player):
        for row in board:
            player_count = 0
            for el in row:
                if el == player:
                    player_count += 1
                    if player_count == self.to_win:
                        return True
                else:
                    player_count = 0

        return False

    def isWin(self, board, player):
        return (self.winsRow(board, player) or self.winsColumn(board, player) 
            or self.winsDiagonal(board, player))

    def isValid(self, row, column, board):
        if 0 > row >= len(board) or 0 > column >= len(board[0]):
            return False
        return True

    def getMove(self, row, column, board):
        if self.isValid(row, column, board) and board[row][column] == EMPTY:
            return (row, column)
        else:
            return ()

    


class TicTacToe(Game):
    def __init__(self):
        super(TicTacToe, self).__init__(3, 3, 3)
        self.indices = [(i,j) for i in range(self.cols) for j in range(self.rows)]

class Connect4(Game):
    def __init__(self):
        super(Connect4, self).__init__(6, 7, 4)
        self.indices = [(0,i) for i in range(self.cols)]

    def lowestRow(self, board, column):
        if column[0] != EMPTY:
            return -1
        row_move = 0
        for i,row in enumerate(board):
            if row == EMPTY:
                row_move = i

        return row_move

    def getMove(self, row, column, board):
        if self.isValid(row, column):
            if (row := self.lowestRow(board, column)) == -1:
                raise IndexError("Column is full")
            return (row, column)
        else:
            return ()

# game = TicTacToe()
