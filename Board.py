import numpy as np


class Board:
    def __init__(self):
        """
        The Board class of which the board we'll use will be an instance of.

        It will keep track of the positions of the pieces on the board, number of plies already played
        and the player whose turn it is to play.
        """
        self._position = np.zeros((3, 3), dtype=int)  # tracked using a 3X3 numpy array with zeroes for blank spaces
        self._avatar = [" ", "X", "O"]  # the type of player or blank space is the index of the needed symbol
        self._current_player = 1  # 1 for the first player and -1 for the second because it will help with the logic
        self._ply = 0

    def print_board(self):
        """
        displays the board position using lines and dashes

        calls needed symbols from the _avatar attribute indexed by the occupant of the position
        """
        print(f"{self._avatar[self._position[(0, 0)]]}|{self._avatar[self._position[(0, 1)]]}|"
              f"{self._avatar[self._position[(0, 2)]]}")
        print("-+-+-")
        print(f"{self._avatar[self._position[(1, 0)]]}|{self._avatar[self._position[(1, 1)]]}|"
              f"{self._avatar[self._position[(1, 2)]]}")
        print("-+-+-")
        print(f"{self._avatar[self._position[(2, 0)]]}|{self._avatar[self._position[(2, 1)]]}|"
              f"{self._avatar[self._position[(2, 2)]]}")

    def get_moves(self):
        """
        returns a list of the moves available in the position

        the last line converts the numpy position to the cardinal position counted from 1 at the
        top left to 9 at the bottom right
        """
        x, y = np.where(self._position == 0)
        return [(3 * x[i] + y[i] + 1) for i in range(len(x))]

    def make_move(self, move):
        """
        changes the value of the specified ordinal position in _position attribute to the value of the current player

        updates the _ply attribute and _current_player
        """
        self._ply += 1
        x, y = divmod(move - 1, 3)  # the minus one accounts for python's indexing
        self._position[(x, y)] = self._current_player
        self._current_player *= -1

    def current_player(self):
        """
        returns the current player as a boolean to help with logic
        """
        if self._current_player == 1:
            return True
        return False

    def is_game_over_win(self):
        """
        returns if a player has won the game as a tuple of 2 values

        the first value represents if the game has been won at all,
        the second value represents who just won the game

        the working principle is that a win will correspond to a line on the position array adding up to 3 or -3
        with 3 as a win for a first player and 3 as a win for the second player
        """
        for i in range(3):
            x = complete_comparer(sum(self._position[(i, j)] for j in range(3)), 3)
            if x[0]:
                return x  # accounts for horizontal wins
            x = complete_comparer(sum(self._position[(j, i)] for j in range(3)), 3)
            if x[0]:
                return x  # accounts for vertical wins
        x = complete_comparer(sum(self._position[(j, j)] for j in range(3)), 3)
        if x[0]:
            return x  # accounts for a win on the leading diagonal
        x = complete_comparer(sum(self._position[(j, 2 - j)] for j in range(3)), 3)
        if x[0]:
            return x  # accounts for a win on the other diagonal
        return False, False

    def is_game_over_draw(self):
        """
        checks if the position has been drawn
        """
        if 0 not in self._position:  # checks for empty spaces
            if not self.is_game_over_win()[0]:  # checks if there hasn't been a win
                return True
        return False

    def undo(self, move):
        """
        undoes a specified move, mainly a requirement for the minimax algorithm
        """
        self._ply -= 1  # reverses the increase in the number of plies
        x, y = divmod(move - 1, 3)
        self._position[(x, y)] = 0
        self._current_player *= -1  # changes back the player to play

    def print_move_count(self):
        """
        displays the move_count
        """
        print(f"Move: {round(self._ply/2 + 0.1) }")  # the 0.1 compensates for tying the round function to even numbers


def complete_comparer(x, y):
    """
    a helper function for evaluating the logic of a win,

    returns 2 values the first indicates if x and y have the same magnitude,
    the second indicates if they are the exact same number i.e. same sign as well
    """
    if abs(x) == y and x == y:
        return True, True
    if abs(x) == y and x == -y:
        return True, False
    return False, False
