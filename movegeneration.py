from evaluation import evaluate
import random
import chess

def Minimax_Get_Move(game_state, depth, player_color):
    
    if depth == 0 or game_state.is_game_over():
        return None, evaluate(game_state)

    
    legal_moves = list(game_state.legal_moves)
    best_move = None
    best_evaluation = float('-inf') if player_color == chess.WHITE else float('inf')
    for move in legal_moves:
        new_game_state = game_state.copy()
        new_game_state.push(move)

        
        _, evaluation = Minimax_Get_Move(new_game_state, depth - 1, player_color)


        if player_color == chess.WHITE:
            if evaluation > best_evaluation:
                best_evaluation = evaluation
                best_move = move
        else:
            if evaluation < best_evaluation:
                best_evaluation = evaluation
                best_move = move

    return best_move, best_evaluation
    
