# This file will have my engine play against previous versions of itself, letting me measure improvement
# 'previous.py' is my file with previous versions of my engine. You can fork and add your own engine to play Mine!

import movegeneration
import previous
import chess
import chess.pgn
import math
def playGame():
    position = chess.Board()
    while not position.is_game_over():
        move, _ = previous.Minimax_Get_Move(position, 4, chess.WHITE, -math.inf, math.inf)
        print(move)
        if move is not None:
            position.push(move)
            
        print(position)
        print(movegeneration.evaluate(position))
        print("\n-----------------\n")
        move, _ = movegeneration.Minimax_Get_Move(position, 4, chess.BLACK, -math.inf, math.inf)
        print(move)
        if move is not None:
            position.push(move)
            
        print(position)
        print(movegeneration.evaluate(position))
        print(position.fen)
        print("\n-----------------\n")
playGame()
