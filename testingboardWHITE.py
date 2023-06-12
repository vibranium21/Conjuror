import chess
import math
from movegeneration import Minimax_Get_Move

def play_game():
    board = chess.Board()

    while not board.is_game_over():
        move, _ = Minimax_Get_Move(board, 4, chess.WHITE, -math.inf, math.inf)
        
        if move is not None:
            board.push(move)
        
        print(board)
        print("\n-----------------\n")

        if board.is_game_over():
            break
        
        valid_move = False
        while not valid_move:
            try:
                user_move = input("Enter your move (in UCI notation): ")
                move = chess.Move.from_uci(user_move)
                if move in board.legal_moves:
                    valid_move = True
                    board.push(move)
                else:
                    print("Invalid move. Try again.")
            except:
                print("Invalid move format. Try again.")

        print(board)
        print("\n-----------------\n")

play_game()


