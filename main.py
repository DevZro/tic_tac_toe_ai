from Board import Board
import random
from bots import ab_negamax, minimax, negamax


def comp_make_move(board, bot_func, move_list):
    """
    makes a move for the bot
    
    takes in the board object and function the bot will be using as inputs
    also takes in the 'move_list' which keeps track of all the moves the player or computer has played
    """
    comp_move = bot_func(board)[1]  # grabs the recommended move from the minimax function
    board.make_move(comp_move)
    move_list.append(comp_move)  # updates the scope of available moves


my_board = Board()  # creates an instance of the board that we'll use
decider = random.randint(0, 1)  # a random binary decider for who gets to start first, bot or human
played_moves = []

if decider:
    """
    if the decider is one, it gets treated as a true and activates this block,

    that leads to the bot playing first but everything else remains the same
    """
    comp_make_move(my_board, ab_negamax, played_moves)
    my_board.print_move_count()

while True:
    """
    the body of the code,
    the theatre where the game is played

    exit functions are placed strategically to break out of the loop after termination points because the loop
    is fundamentally infinite, instead of having a is_game-over variable
    """
    my_board.print_board()
    while True:
        try:
            # the bug catching block to avoid weird moves
            move = int(input("Where would you like to play? "))
            if move not in played_moves and move in range(0, 10):  # stops already played inputs or strange inputs
                played_moves.append(move)
                my_board.make_move(move)
                break  # only after eventually passing the requirements will the move be inputted and the while loop end
            else:
                print("You made an invalid move, try again.")
        except ValueError:
            print("You made an invalid move, try again.")
    my_board.print_move_count()
    my_board.print_board()
    if my_board.is_game_over_win()[0]:
        print("Congratulations you win!")  # the second output isn't needed, only the human can win after she plays
        exit()
    if my_board.is_game_over_draw():
        print("Draw!")
        exit()
    comp_make_move(my_board, ab_negamax, played_moves)
    if my_board.is_game_over_win()[0]:
        my_board.print_board()
        print("You lose, maybe next time")  # the second output isn't needed, only the bot can win after it plays
        exit()
    if my_board.is_game_over_draw():
        my_board.print_board()
        print("Draw!")
        exit()
