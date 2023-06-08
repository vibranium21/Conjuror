import chess
import math
piece_values = {
    chess.PAWN: 150,
    chess.ROOK: 490,
    chess.KNIGHT: 270,
    chess.BISHOP: 330,
    chess.QUEEN: 900,
    chess.KING: 20000
}
knight_piece_square_table = [
-45, -30, -25, -25, -25, -25, -30, - 45,
-30, -15, 0, 0, 0, 0, -15, -30,
-25, 0, 20, 20, 20, 20, 0, -25,
-25, 0, 15, 20, 20, 15, 0, -25,
-25, 0, 15, 20, 20, 15, 0, -25,
-25, 0, 20, 20, 20, 20, 0, -25,
-30, -15, 0, 0, 0, 0, -15, -30,
-45, -30, -25, -25, -25, -25, -30, - 45
]
white_pawn_table = [
    0,  0,  0,  0,  0,  0,  0,  0,
    5, 10, 10, -20, -20, 10, 10,  5,
    5, -5, -10,  0,  0, -10, -5,  5,
    0,  0,  0, 20, 20,  0,  0,  0,
    5,  5, 10, 22, 22, 10,  5,  5,
    10, 10, 20, 25, 25, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0
]

black_pawn_table = list(reversed(white_pawn_table))

bishop_table = [
    # score = (squares with possible movement-10)*5
    # A few exceptions on long diagonals though.
-15, -15, -15, -15, -15, -15, -15, -15,
-15, 12, -5, -5, -5, -5, 12, -15,
-15, -5, 5, 5, 5, 5, -5, -15,
-15, -5, 15, 15, 15, 15, -5, -15,
-15, -5, 15, 15, 15, 15, -5, -15,
-15, -5, 5, 5, 5, 5, -5, -15,
-15, 12, -5, -5, -5, -5, 12, -15,
-15, -15, -15, -15, -15, -15, -15, -15
]
rookEvalWhite = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 5, 5, 0, 0, -5,
    -5, 0, 0, 5, 5, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0
]
rookEvalBlack = list(reversed(rookEvalWhite))


queenEval = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -5, 0, 5, 5, 5, 5, 0, -5,
    -5, 0, 5, 5, 5, 5, 0, -5,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -10, 0, 5, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20
]

kingEvalWhite = [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30
]
kingEvalBlack = list(reversed(kingEvalWhite))

def evaluate_piece(piece: chess.Piece, square: chess.Square):
    mapping = []
    if piece.piece_type == chess.PAWN:
        mapping = white_pawn_table if piece.color == chess.WHITE else black_pawn_table
    elif piece.piece_type == chess.KNIGHT:
        mapping = knight_piece_square_table
    elif piece.piece_type == chess.BISHOP:
        mapping = bishop_table
    elif piece.piece_type == chess.QUEEN:
        mapping = queenEval
    elif piece.piece_type == chess.KING:
        mapping = kingEvalWhite if piece.color == chess.WHITE else kingEvalBlack
    elif piece.piece_type == chess.ROOK:
        mapping = rookEvalWhite if piece.color == chess.WHITE else rookEvalBlack
    return mapping[square]



    


    


def evaluate(game_state):
    eval = 0
    for square in chess.SQUARES:
        piece = game_state.piece_at(square)
        if not piece:
            continue
        if piece.color == chess.WHITE:
            eval += piece_values[piece.piece_type]
            eval += evaluate_piece(piece, square)  # Pass piece and square arguments
        else:
            eval -= piece_values[piece.piece_type]
            eval -= evaluate_piece(piece, square)  # Pass piece and square arguments
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

    
