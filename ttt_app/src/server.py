from flask import Flask, jsonify
import tictactoe as ttt

app = Flask(__name__)

curr_game = ttt.MiniMax()

# return winner if applicable, or if it is a draw
@app.route("/get_status")
def get_status():
    return "<p>Hello, World!</p>"

# return game board
@app.route("/start_game")
def start_game():
    curr_game = ttt.MiniMax()
    return curr_game.get_board()

# return game board
@app.route("/player_move")
def player_move(row, col):
    curr_game.mark_square(row, col, curr_game.PLAYER)
    return curr_game.get_board()

# return game board
@app.route("/ai_move")
def ai_move():
    curr_game.alpha_beta()
    print(curr_game.get_board())
    return jsonify(curr_game.get_board())