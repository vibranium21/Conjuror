from evaluation import evaluate


def minimax(depth, board, maximizing_player, minimizing_color ):
    if depth == 0 or board.gameover:
        return None, evaluate()
    
