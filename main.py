import os
from stockfish import Stockfish
from dotenv import load_dotenv


load_dotenv()
sfPath = os.environ.get("SF_PATH", "stockfish\\stockfish-windows-x86-64-avx2.exe")
sf = Stockfish(sfPath)
