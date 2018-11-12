"""
The module that holds the generic structure for the state class.
"""
from typing import List, Any


class CurrentState:
    """ Represents the current state of an arbitrary game.

    possible_moves - a list of the possible moves to make
    current_player - the player who has the current turn to play
    """

    current_player: str

    def __init__(self, is_p1_turn: bool) -> None:
        """ Initializes the Game class.
        """
        if is_p1_turn:
            self.current_player = 'p1'
        else:
            self.current_player = 'p2'

    def __str__(self) -> str:
        """ Outputs the string representation of Game.
        """
        raise NotImplementedError("Specified current_state must have a " +
                                  "__str__ method!")

    def __eq__(self, other: "CurrentState") -> bool:
        """ Returns True iff two Game objects are equal, False otherwise.
        """
        raise NotImplementedError("Specified current_state must have a " +
                                  "__eq__ method!")

    def get_current_player_name(self) -> str:
        """ Returns who the current player is in the current state of the game.
        """
        raise NotImplementedError("Specified current_state must have a " +
                                  "get_current_player_name method!")

    def get_possible_moves(self) -> List[str]:
        """ Returns all possible (legal) moves to be made in
        the current state of the game.
        """
        raise NotImplementedError("Specified current_state must have a " +
                                  "get_possible_moves method!")

    def is_valid_move(self, move: Any) -> bool:
        """ Returns True iff the given move is a valid move
        of the current state.
        """
        raise NotImplementedError("Specified current_state must have a " +
                                  "is_valid_move method!")

    def make_move(self, move: Any) -> "CurrentState":
        """ Updates the current state of the game by
        implemented the given move."""
        raise NotImplementedError("Specified current_state must have a " +
                                  "make_move method!")


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
