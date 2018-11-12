"""
The main module representing a generic game.
"""
from typing import Any
from current_state import CurrentState


class Game:
    """ Represents a the structure of a generic game class to be inherited from.

    current_state - represents the current state of the game.
    """

    current_state: CurrentState

    def __init__(self, is_p1_turn: bool) -> None:
        """ Initializes the Game class.
        """
        self.current_state = CurrentState(is_p1_turn)
        raise NotImplementedError("Specified game must have a __init__ method!")

    def __str__(self) -> str:
        """ Outputs the string representation of Game.
        """
        raise NotImplementedError("Specified game must have a __str__ method!")

    def __eq__(self, other: "Game") -> bool:
        """ Determines if two Game objects are equal.
        """
        raise NotImplementedError("Specified game must have a __eq__ method!")

    def get_instructions(self) -> str:
        """ Returns the instructions on how to play the specified Game.
        """
        raise NotImplementedError("Specified game must have a " +
                                  "get_instructions method!")

    def is_over(self, current_state: CurrentState) -> bool:
        """ Returns the instructions on how to play the specified Game.
        """
        raise NotImplementedError("Specified game must have a is_over method!")

    def str_to_move(self, move: Any) -> int:
        """ Returns a the converted type and format from a given str move.
        """
        raise NotImplementedError("Specified game must have a " +
                                  "str_to_move method!")

    def is_winner(self, player: Any) -> bool:
        """ Returns True iff the given player is the winner of the game.
        """
        raise NotImplementedError("Specified game must have a " +
                                  "is_winner method!")


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
