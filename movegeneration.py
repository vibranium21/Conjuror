import random
import chess

piece_values = {
    chess.PAWN: 150,
    chess.ROOK: 490,
    chess.KNIGHT: 270,
    chess.BISHOP: 330,
    chess.QUEEN: 900,
    chess.KING: 20000
}

def evaluate(game_state):
    eval = 0
    for square in chess.SQUARES:
        piece = game_state.piece_at(square)
        if not piece:
            continue
        if piece.color == chess.WHITE:
            eval += piece_values[piece.piece_type]
        else:
            eval -= piece_values[piece.piece_type]
    return eval

def Minimax_Get_Move(game_state, depth, player_color, alpha, beta):
    if depth == 0 or game_state.is_game_over():
        return None, evaluate(game_state)

    legal_moves = list(game_state.legal_moves)
    best_move = None
    for move in legal_moves:
        new_game_state = game_state.copy()
        new_game_state.push(move)

        _, evaluation = Minimax_Get_Move(new_game_state, depth - 1, player_color, alpha, beta)

        if player_color == chess.WHITE:
            if evaluation > alpha:
                alpha = evaluation
                best_move = move
        else:
            if evaluation < beta:
                beta = evaluation
                best_move = move

        if alpha >= beta:
            break

    return best_move, alpha
