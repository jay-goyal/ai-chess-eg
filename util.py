import chess


def generateFen(K, Q, k):
    board_pos = [["." for _ in range(8)] for _ in range(8)]
    board_pos[K // 8][K % 8] = "K"
    board_pos[Q // 8][Q % 8] = "Q"
    board_pos[k // 8][k % 8] = "k"
    ans = ""
    for row in board_pos:
        count_empty = 0
        for cell in row:
            if cell == ".":
                count_empty += 1
            else:
                if count_empty > 0:
                    ans += str(count_empty)
                    count_empty = 0
                ans += cell
        if count_empty > 0:
            ans += str(count_empty)
        ans += "/"

    ans = ans[:-1]  # Remove the last '/'
    ans += " w - - 0 1"
    return ans


def inKingRange(K, k):
    if abs(K // 8 - k // 8) <= 1 and abs(K % 8 - k % 8) <= 1:
        return True
    return False


def inQueenRange(Q, k):
    # TODO: Better Checks
    if Q // 8 == k // 8 or Q % 8 == k % 8:
        return True
    if Q // 8 - Q % 8 == k // 8 - k % 8 or Q // 8 + Q % 8 == k // 8 + k % 8:
        return True
    return False


def fenCheck(K, Q, k):
    if inKingRange(K, k) or inQueenRange(Q, k):
        return False
    return True


def getMatRepFen(fen):
    matrix = [["."] * 8 for _ in range(8)]
    inp = fen.split()[0]
    row = 0
    col = 0

    for char in inp:
        if char.isdigit():
            col += int(char)
        elif char == "/":
            row += 1
            col = 0
        else:
            matrix[row][col] = char
            col += 1

    return matrix


def whoPlayedLast(fen):
    x = fen.split()[1]
    if x == "w":
        return "BLACK"
    return "WHITE"


def checkMate(stockfish):
    evaluation = stockfish.get_evaluation()
    if evaluation["type"] == "mate" and evaluation["value"] == 0:
        return True
    return False


def checkStalemate(stockfish):
    # TODO: Implement method
    pass


def printBoard(stockfish, chessBoard, pref):
    if pref.lower() == "stockfish":
        print(stockfish.get_board_visual())
    else:
        print(chessBoard)
