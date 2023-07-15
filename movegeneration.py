import chess
import math

safeKing = 150
bishopPair = 70
piece_values = {
    chess.PAWN: 100,
    chess.ROOK: 500,
    chess.KNIGHT: 270,
    chess.BISHOP: 340,
    chess.QUEEN: 950,
    chess.KING: 200000
}
kingEvalEndGame = [
    -150, -30, -30, -30, -30, -30, -30, -150,
    -30, -30,  0,  0,  0,  0, -30, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -20, -10,  0,  0, -10, -20, -30,
    -150, -140, -70, -10, -10, -70, -140, -150
]

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
    30, 80, 100, 150, 150, 100, 80, 30,
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


chess.WHITE: chess.Color= True
chess.BLACK: chess.Color= False
def WhiteBishopPair(position):
    white_bishops = 0

    for square in chess.SQUARES:
        piece = position.piece_at(square)

        if piece is not None and piece.piece_type == chess.BISHOP and piece.color == chess.WHITE:
            white_bishops += 1

    return white_bishops >= 2


        
def BlackBishopPair(position):
    black_bishops = 0

    for square in chess.SQUARES:
        piece = position.piece_at(square)

        if piece is not None and piece.piece_type == chess.BISHOP and piece.color == chess.BLACK:
            black_bishops += 1

    return black_bishops >= 2
def WhiteKingIsSafe(position):
    piece_map = position.piece_map()
    safe_king_score = 0
    for square in chess.SQUARES:
        piece = position.piece_at(square)
        if piece is not None and  piece.piece_type == chess.KING and piece.color == chess.WHITE:
            if str(piece_map.get(square+9)) is not None and  not str(piece_map.get(square+9)).lower():
                safe_king_score +=1
            if str(piece_map.get(square+8)) is not None and  not str(piece_map.get(square+8)).lower():
                safe_king_score += 1
            if str(piece_map.get(square+7)) is not None and not str(piece_map.get(square+7)).lower():
                safe_king_score += 1
            if str(piece_map.get(square+16)) is not None and not str(piece_map.get(square+16)).lower():
                safe_king_score -= 1
            if str(piece_map.get(square+17)) is not None and not str(piece_map.get(square+17)).lower():
                safe_king_score -= 1
            if str(piece_map.get(square+15)) is not None and not str(piece_map.get(square+15)).lower():
                safe_king_score -= 1
    return safe_king_score > 1
def BlackKingIsSafe(position):
    piece_map = position.piece_map()
    safe_king_scoreBlack = 0
    for square in chess.SQUARES:
        piece = position.piece_at(square)
        if piece is not None and  piece.piece_type == chess.KING and piece.color == chess.BLACK:
            if str(piece_map.get(square-9)) is not None and  not str(piece_map.get(square-9)).upper():
                safe_king_scoreBlack +=1
            if str(piece_map.get(square-8)) is not None and  not str(piece_map.get(square-8)).upper():
                safe_king_scoreBlack += 1
            if str(piece_map.get(square-7)) is not None and not str(piece_map.get(square-7)).upper():
                safe_king_scoreBlack += 1
            if str(piece_map.get(square-16)) is not None and not str(piece_map.get(square-16)).lower():
                safe_king_scoreBlack -= 1
            if str(piece_map.get(square-17)) is not None and not str(piece_map.get(square-17)).lower():
                safe_king_scoreBlack -= 1
            if str(piece_map.get(square-15)) is not None and not str(piece_map.get(square-15)).lower():
                safe_king_scoreBlack -= 1
    return safe_king_scoreBlack > 1
            


            




def evaluate_piece(piece: chess.Piece, square: chess.Square, position):
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
        if check_end_game(position) == True:
            mapping = kingEvalEndGame    
        else: 
            if piece.color == chess.WHITE:
                mapping = kingEvalWhite
            if piece.color == chess.BLACK:
                mapping = kingEvalBlack
    elif piece.piece_type == chess.ROOK:
        mapping = rookEvalWhite if piece.color == chess.WHITE else rookEvalBlack
    return mapping[square]

def check_end_game(board: chess.Board):
    queens = 0
    minors = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece and piece.piece_type == chess.QUEEN:
            queens += 1
        if piece and (
            piece.piece_type == chess.BISHOP or piece.piece_type == chess.KNIGHT
        ):
            minors += 1

    if queens == 0 or (queens == 2 and minors <= 1):
        return True

    return False



def evaluate(position):
    eval = 0
    if position.is_checkmate():
        return -math.inf
    if position.is_stalemate():
        return 0
    if position.is_fivefold_repetition():
        return 0
    if WhiteKingIsSafe(position):
        eval += safeKing
    else:
        eval -= safeKing
    if BlackKingIsSafe(position):
        eval -= safeKing
    else: 
        eval += safeKing
    BlackBishopsPair = BlackBishopPair(position)
    WhiteBishopsPair = WhiteBishopPair(position)
    if BlackBishopsPair == True:
        eval -= bishopPair
    elif WhiteBishopsPair == True:
        eval += bishopPair
    for square in chess.SQUARES:
        piece = position.piece_at(square)
        if not piece:
            continue
        if piece.color == chess.WHITE:
            eval += piece_values[piece.piece_type]
            eval += evaluate_piece(piece, square, position)  # Pass piece and square arguments
        else:
            eval -= piece_values[piece.piece_type]
            eval -= evaluate_piece(piece, square, position)  # Pass piece and square arguments
    return eval if position.turn == chess.WHITE else  -eval

def order_moves(position, moves):
    ordered_moves = []
    
    # Prioritize capturing moves
    PotentiallyGood_moves = []

    for move in moves:
        if position.is_capture(move):
            PotentiallyGood_moves.append(move)
        if position.is_check():
            PotentiallyGood_moves.append(move)
        else:
            ordered_moves.append(move)
    
    ordered_moves.extend(PotentiallyGood_moves)
    return ordered_moves






def Minimax_Get_Move(position, depth, player_color, alpha, beta):
    movessearched = 0
    movessearched +=1

    if depth == 0 or position.is_game_over():
        return None, evaluate(position)  
    

    legal_moves = order_moves(position, position.legal_moves)
    best_move = None

    # Check for captures or significant changes in the position
    if depth <= 0 and (position.is_check() or position.is_capture() or position.is_checkmate()):
        return None, evaluate(position)

    for move in legal_moves:
        position.push(move)
        
        _, evaluation = Minimax_Get_Move(position, depth - 1, player_color, -beta, -alpha)
        evaluation = -evaluation
        position.pop()

        if evaluation > alpha:
            alpha = evaluation
            best_move = move
        if alpha >= beta:
            break
                    
    return best_move, alpha
