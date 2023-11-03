import os
from stockfish import Stockfish
from dotenv import load_dotenv
import chess
import random
import util


load_dotenv()
sfPath = os.environ.get("SF_PATH", "stockfish\\stockfish-windows-x86-64-avx2.exe")
printPref = os.environ.get("PRINT_PREF", "chess")

stockfish = Stockfish(sfPath)

# Initialize Board
K, Q, k = -1, -1, -1
while not util.fenCheck(K, Q, k):
    K, Q, k = random.sample(range(0, 63), 3)

fen = util.generateFen(K, Q, k)
stockfish.set_fen_position(fen)
board = chess.Board(fen)

os.system("cls" if os.name == "nt" else "clear")
print(stockfish.get_best_move())
print(stockfish.get_evaluation())
print(fen)
util.printBoard(stockfish, board, printPref)

# Play the game
while not util.checkMate(stockfish):
    print("Press any key for next position")
    input()
    os.system("cls" if os.name == "nt" else "clear")
    evaluation = stockfish.get_evaluation()
    stockfish.make_moves_from_current_position([stockfish.get_best_move()])
    board = chess.Board(stockfish.get_fen_position())
    if util.checkMate(stockfish):
        print(
            "CHECK MATE. ",
            util.whoPlayedLast(stockfish.get_fen_position()),
            " WINS!",
        )
    print(stockfish.get_fen_position())
    util.printBoard(stockfish, board, printPref)

print("GAME OVER")
