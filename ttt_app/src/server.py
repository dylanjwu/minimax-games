from flask import Flask, jsonify, request
import minimax as ai
import Game as game
from utils import *
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


curr_game = game.Game(3,3,3)

# return winner if applicable, or if it is a draw
@app.route("/get_status")
def get_status():
    return "<p>Hello, World!</p>"

# return game board
@app.route("/start_game")
def start_game():
    global curr_game

    curr_game.clear()
    kind = "tic-tac-toe"
    print("START")
    if kind == "tic-tac-toe":
        curr_game = game.TicTacToe()
    else:
        curr_game = game.Connect4()

    return jsonify(curr_game.getBoard())

# return game board
@app.route("/player_move", methods = ['POST'])
def player_move():
    global curr_game

    print(curr_game.getBoard())
    data = request.get_json()
    index = data['index']
    c = 0
    row, col = 0, 0
    for i in range(curr_game.rows):
        for j in range(curr_game.cols):
            if c == index:
                row = i
                col = j
            c += 1

    curr_game.markSquare(row, col, PLAYER)
    return jsonify(curr_game.getBoard())

# return game board
@app.route("/ai_move")
def ai_move():
    print(curr_game.getBoard())
    row, col = ai.AI(curr_game).alpha_beta()
    print(row, col)
    if row == None or col == None:
        return jsonify(curr_game.getBoard())
    curr_game.markSquare(row, col, COMP)
    return jsonify(curr_game.getBoard())

