import numpy as np
import random

# contains all the possible approaches the bot can implement


def minimax(board):
    """
    textbook minimax function but with just one input,
    the player is not needed because that can be gotten from the board instance,
    the depth is not needed because tic-tac-toe is simple enough to solve perfectly
    """
    if board.is_game_over_draw():
        return random.uniform(0, 0.1), None
        # a random small number is returned instead of zero to urge the bot the try different moves in drawn position,
        # similar to a human trying different things to throw their opponent off rather than making the same draw always
    if board.is_game_over_win()[0]:
        if board.is_game_over_win()[1]:
            return 1, None
        return -1, None
        # playing the same move in wining positions potential gives the bot less "character" but will ultimately suffice

    best_move = None
    if board.current_player():
        best_score = -np.inf
    else:
        best_score = np.inf

    for move in board.get_moves():
        board.make_move(move)

        current_score, current_move = minimax(board)
        board.undo(move)

        if board.current_player():
            if current_score > best_score:
                best_score = current_score
                best_move = move
        else:
            if current_score < best_score:
                best_score = current_score
                best_move = move

    return best_score, best_move


def negamax(board):
    """
    also a textbook negamax function without the other inputs for the same reason as the minimax
    """
    if board.is_game_over_draw():
        return random.uniform(0, 0.1), None
    if board.is_game_over_win()[0]:
        return -1, None

    best_move = None
    best_score = -np.inf

    for move in board.get_moves():
        board.make_move(move)
        recurse_score, current_move = negamax(board)
        board.undo(move)
        current_score = -recurse_score

        if current_score > best_score:
            best_score = current_score
            best_move = move

    return best_score, best_move


def abnegamax(board, alpha, beta):
    """
        again a textbook negamax function with alpha-beta pruning without the other inputs,
        for the same reason as the minimax.

        the alpha and beta parameters were particular impossible to remove though
    """
    if board.is_game_over_draw():
        return random.uniform(0, 0.1), None
    if board.is_game_over_win()[0]:
        return -1, None

    best_move = None
    best_score = -np.inf

    for move in board.get_moves():
        board.make_move(move)
        recurse_score, current_move = abnegamax(board, -beta, -max(alpha, best_score))
        board.undo(move)
        current_score = -recurse_score

        if current_score > best_score:
            best_score = current_score
            best_move = move

        if best_score >= beta:
            return best_score, best_move

    return best_score, best_move


def ab_negamax(board):
    """
    a dummy function designed to hold the abnegamax function in a format that the comp_function can handle.
    """
    return abnegamax(board, -np.inf, np.inf)
