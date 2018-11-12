"""
The implementation of the Subtract Square game.
"""
from typing import List
from game import Game
from current_state import CurrentState


class SubtractSquare(Game):
    """ The SubtractSquare inherited from the generic Game class.

    current_state - the current state of SubtractSquare game inherited
    from the current_state super class.
    """

    current_state: "CurrentSubtractSquareState"

    def __init__(self, is_p1_turn: bool, value: int = -1) -> None:
        """ Initializes the SubtractSquare game.

        >>> new_game = SubtractSquare(True, 10)
        >>> new_game.current_state.current_player
        'p1'
        >>> new_game.current_state.current_number
        10
        """
        # If the object is not created with a specified starting value,
        # Ask the user for one.
        if value == -1:
            value = None
            while not isinstance(value, int):
                value = int(input('Please enter the value to subtract from: '))
        self.current_state = CurrentSubtractSquareState(is_p1_turn, value)

    def __str__(self) -> str:
        """ Outputs the string representation of the SubtractSquare game.

        >>> new_game = SubtractSquare(False, 64)
        >>> str(new_game)
        'Current Standings: Value = 64'
        """
        return "Current Standings: " + self.current_state.__str__()

    def __eq__(self, other: "SubtractSquare") -> bool:
        """ Determines if two SubtractSquare objects are equal.

        >>> game1 = SubtractSquare(True, 10)
        >>> game2 = SubtractSquare(True, 10)
        >>> game1 == game2
        True
        >>> game3 = SubtractSquare(False, 10)
        >>> game1 == game3
        True
        >>> game4 = SubtractSquare(False, 11)
        >>> game1 == game4
        False
        """
        # Checks if both types and (if so) current values are equal.
        return (type(self) == type(other)
                and self.current_state.current_number ==
                other.current_state.current_number)

    def get_instructions(self) -> str:
        """ Returns the instructions on how to play the specified Game.

        >>> game = SubtractSquare(False, 1024)
        >>> print(game.get_instructions())
        To play the Subtract Square game, each player is to
        choose a positive whole number square to deduct from
        the newly random value produced at the beginning of
        the game as long as the number they chose is less
        than the value. Each player alternates in turns until
        there are no moves left to make, in which case the
        player whose turn it would have been loses!
        """
        return ("To play the Subtract Square game, each player is to\n" +
                "choose a positive whole number square to deduct from\n" +
                "the newly random value produced at the beginning of\n" +
                "the game as long as the number they chose is less\n" +
                "than the value. Each player alternates in turns until\n" +
                "there are no moves left to make, in which case the\n" +
                "player whose turn it would have been loses!")

    def is_over(self, current_state: CurrentState) -> bool:
        """ Returns the instructions on how to play the specified Game.

        >>> game1 = SubtractSquare(True, 1)
        >>> game1.is_over(game1.current_state)
        False
        >>> game1.is_over(SubtractSquare(True, 0).current_state)
        True
        """
        # Game over if there are no possible moves left to make.
        return len(current_state.get_possible_moves()) == 0

    def str_to_move(self, move: str) -> int:
        """ Returns a the converted type and format from a given str move.

        >>> move = '16'
        >>> game = SubtractSquare(True, 16)
        >>> game.str_to_move(move)
        16
        """
        # Converts move into a usable type.
        return int(move)

    def is_winner(self, player: str) -> bool:
        """ Returns True iff the given player is the winner of the game.

        >>> game = SubtractSquare(True, 0)
        >>> game.is_winner('p1')
        False
        >>> game.is_winner('p2')
        True
        """
        # As long as the game is over, the player about to play loses.
        return (self.is_over(self.current_state)
                and self.current_state.current_player != player)


class CurrentSubtractSquareState(CurrentState):
    """ The current state class for the SubtractSquare game.

    current_player - the player currently making a move
    current_number - the value left to subtract from
    """

    current_player: str
    current_number: int

    def __init__(self, is_p1_turn: bool, value: int) -> None:
        """ Initializes the current state for the SubtractSquare class.

        >>> state = CurrentSubtractSquareState(True, 5)
        >>> state.current_number
        5
        >>> state.current_player
        'p1'
        """
        # Calls the generic __init__ for initializing the current player.
        CurrentState.__init__(self, is_p1_turn)

        self.current_number = value

    def __str__(self) -> str:
        """ Outputs the string representation of the current state.

        >>> state = CurrentSubtractSquareState(False, 123)
        >>> print(state)
        Value = 123
        """
        return 'Value = ' + str(self.current_number)

    def __eq__(self, other: "CurrentSubtractSquareState") -> bool:
        """ Returns True iff two CurrentSubtractSquareState objects
        are equal, False otherwise.

        >>> state1 = CurrentSubtractSquareState(True, 16)
        >>> state2 = CurrentSubtractSquareState(False, 16)
        >>> state3 = 'CurrentSubtractSquareState(True, 16)'
        >>> state4 = CurrentSubtractSquareState(True, 17)
        >>> state1 == state2
        True
        >>> state1 == state3
        False
        >>> state1 == state4
        False
        """
        # Both types and current numbers attributes of the object equate.
        return (type(self) == type(other)
                and self.current_number == other.current_number)

    def get_current_player_name(self) -> str:
        """ Returns the player who is currently playing at the of the game.

        >>> state = CurrentSubtractSquareState(True, 2)
        >>> state.get_current_player_name()
        'p1'
        >>> state = state.make_move(1)
        >>> state.get_current_player_name()
        'p2'
        """
        return self.current_player

    def get_possible_moves(self) -> List[str]:
        """ Returns all possible (legal) moves to be made in the current state
        of the game. All legal squares to be played in the state.

        >>> state = CurrentSubtractSquareState(False, 36)
        >>> state.get_possible_moves()
        [1, 4, 9, 16, 25, 36]
        >>> state = state.make_move(36)
        >>> state.get_possible_moves()
        []
        """
        # Iterates through the square roots between 0 and the current
        # number and lists the valid squares.
        moves = []
        for i in range(1, int(self.current_number ** 0.5) + 1):
            moves.append(i ** 2)
        return moves

    def is_valid_move(self, move: int) -> bool:
        """ Returns True iff the given move is a valid move of
        the current state, that is, if the square played is in the legal
        bounds between 1 and the current value.

        >>> state = CurrentSubtractSquareState(False, 511)
        >>> state.is_valid_move(512)
        False
        >>> state.is_valid_move(510)
        False
        >>> state.is_valid_move(256)
        True
        """
        # If the move is a square, an int, and less than the current number.
        return (not isinstance(move, type(None))  # type(move) != type(None)
                and 1 <= move <= self.current_number
                and int(move ** 0.5) == move ** 0.5)

    def make_move(self, move: int) -> "CurrentSubtractSquareState":
        """ Updates the current state of the game by provided legal move
        by subtracting the square move from the current value.

        >>> state = CurrentSubtractSquareState(True, 25)
        >>> state = state.make_move(16)
        >>> str(state)
        'Value = 9'
        >>> str(state.make_move(9))
        'Value = 0'
        """
        # Creates a copy of the current state to avoid self mutabilizing.
        import copy
        new_state = copy.copy(self)
        new_state.current_number = self.current_number - move
        if self.current_player == 'p1':
            new_state.current_player = 'p2'
        else:
            new_state.current_player = 'p1'
        return new_state


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")

    import doctest
    doctest.testmod()
