import sqlite3
import random
from difflib import SequenceMatcher
import unicodedata
import pandas as pd
import numpy as np
import chess
import chess.engine
import chess.pgn
import chess.svg
import sklearn
from sklearn.linear_model import LogisticRegression
pgn = open("pgn/Modern.pgn")

#engine = chess.engine.SimpleEngine.popen_uci("/usr/bin/stockfish")

RANDOM_SEED = 0
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

conn = sqlite3.connect('data.db')
c = conn.cursor()

def get_fen(num_games):
    fen_arr = []
    result_arr = []
    for i in range(num_games):
        game = chess.pgn.read_game(pgn)
        board = game.board()
        if game.headers["Result"] == '1-0':
            result = 1
        elif game.headers["Result"] == '0-1':
            result = -1
        else:
            continue
        for j in game.mainline_moves():
            board.push(j)
            fen = board.board_fen()
            fen_arr.append(fen)
            result_arr.append(result)
    return fen_arr, result_arr

def fen_to_matrix(inputstr):
    pieces_str = "PNBRQK"
    pieces_str += pieces_str.lower()
    pieces = set(pieces_str)
    valid_spaces = set(range(1, 9))
    pieces_dict = {pieces_str[0]: 1, pieces_str[1]: 2, pieces_str[2]: 3, pieces_str[3]: 4,
                   pieces_str[4]: 5, pieces_str[5]: 6,
                   pieces_str[6]: -1, pieces_str[7]: -2, pieces_str[8]: -3, pieces_str[9]: -4,
                   pieces_str[10]: -5, pieces_str[11]: -6}

    boardtensor = np.zeros((8, 8, 6, 2))

    inputliste = inputstr.split()
    rownr = 0
    colnr = 0
    for i, c in enumerate(inputliste[0]):
        if c in pieces:
            if np.sign(pieces_dict[c]) == 1:
                boardtensor[rownr, colnr, np.abs(pieces_dict[c]) - 1, 0] = np.sign(pieces_dict[c])
            else:
                boardtensor[rownr, colnr, np.abs(pieces_dict[c]) - 1, 1] = -np.sign(pieces_dict[c])
            colnr = colnr + 1
        elif c == '/':  # new row
            rownr = rownr + 1
            colnr = 0
        elif int(c) in valid_spaces:
            colnr = colnr + int(c)
        else:
            raise ValueError("invalid fenstr at index: {} char: {}".format(i, c))
    return boardtensor

def get_board_matrix(fen):
    board = []
    for i in fen:
        board.append(fen_to_matrix(i))
    return board

def get_X_y(result, board):
    X = []
    y = []
    for i in range(len(board)):
        X.append(np.reshape(board[i], 768))
        y.append(result[i])
    return X, y


def main():
    fen, result = get_fen(2000)
    print(result)
    board = get_board_matrix(fen)
    #b = game.board()
    #svg = chess.svg.board(board=b, size=400)
    X, y = get_X_y(result, board)
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.25, random_state=0)

    lr = LogisticRegression(solver='lbfgs', max_iter=1000)
    lr = lr.fit(X_train, y_train)
    y_pred_test = lr.predict(X_test)
    y_targ_test = y_test
    testing_acc = (y_pred_test == y_targ_test).sum() / len(y_pred_test)
    print(f'testing accuracy:  {testing_acc}')


if __name__=='__main__':
    main()

