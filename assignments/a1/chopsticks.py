"""
The implementation of the Chopsticks game.
"""
from typing import List, Dict
from game import Game
from current_state import CurrentState

# Constants to be used for hand differentiation.
LEFT_HAND = 0
RIGHT_HAND = 1


class Chopsticks(Game):
    """ The Chopsticks class inherited from the generic Game class.

    current_state - the current state specified for the Chopsticks game
    from the super class CurrentState
    """

    current_state: "CurrentChopsticksState"

    def __init__(self, is_p1_turn: bool) -> None:
        """ Initializes the Chopsticks game.

        >>> game = Chopsticks(True)
        >>> game.current_state.current_player
        'p1'
        """
        self.current_state = CurrentChopsticksState(is_p1_turn)

    def __str__(self) -> str:
        """ Outputs the string representation of the Chopsticks game.

        >>> game = Chopsticks(False)
        >>> str(game)
        'The current standings are: Player 1: 1 - 1; Player 2: 1 - 1'
        >>> game.current_state = game.current_state.make_move('rr')
        >>> str(game)
        'The current standings are: Player 1: 1 - 2; Player 2: 1 - 1'
        """
        return "The current standings are: " + self.current_state.__str__()

    def __eq__(self, other: "Chopsticks") -> bool:
        """ Determines if two Chopsticks objects are equal from their
        current states of the player and player hands.

        >>> game1 = Chopsticks(True)
        >>> game2 = Chopsticks(True)
        >>> game1 == game2
        True
        >>> game1.current_state = game1.current_state.make_move('lr')
        >>> game1 == game2
        False
        >>> game3 = Chopsticks(False)
        >>> game1 == game3
        False
        """
        # Determines if the type and current states of the objects equate.
        return (type(self) == type(other)
                and self.current_state.__eq__(other.current_state))

    def get_instructions(self) -> str:
        """ Returns the instructions on how to play the Chopsticks Game.

        >>> game = Chopsticks(True)
        >>> print(game.get_instructions())
        To play the Chopsticks game, the first player
        uses one hand to touch one of the second player's
        hand and adds fingers based on the total fingers
        up on the dealing and receiving hand. A player's
        hand is 'dead' only if the fingers up hits exactly
        five and the first player to have two 'dead' loses!
        """
        return ("To play the Chopsticks game, the first player\n" +
                "uses one hand to touch one of the second player's\n" +
                "hand and adds fingers based on the total fingers\n" +
                "up on the dealing and receiving hand. A player's\n" +
                "hand is 'dead' only if the fingers up hits exactly\n" +
                "five and the first player to have two 'dead' loses!")

    def is_over(self, current_state: CurrentState) -> bool:
        """ Returns the instructions on how to play the specified Game.

        >>> game = Chopsticks(True)
        >>> game.is_over(game.current_state)
        False
        >>> game.current_state = game.current_state.make_move('ll')
        >>> game.current_state = game.current_state.make_move('ll')
        >>> game.current_state = game.current_state.make_move('ll')
        >>> game.current_state = game.current_state.make_move('rl')
        >>> game.current_state = game.current_state.make_move('lr')
        >>> game.is_over(game.current_state)
        True
        """
        # Game over if no more moves can be made.
        return current_state.get_possible_moves() == []

    def str_to_move(self, move: str) -> str:
        """ Returns a converted move type and format from a given str move.

        >>> game = Chopsticks(True)
        >>> game.str_to_move('  Rr   ')
        'rr'
        """
        # Cleans and makes the format for move valid.
        return move.lower().strip()

    def is_winner(self, player: str) -> bool:
        """ Returns True iff the given player is the winner of the game.

        >>> game = Chopsticks(True)
        >>> game.is_winner('p1')
        False
        >>> game.is_winner('p2')
        False
        >>> game.current_state = game.current_state.make_move('ll')
        >>> game.current_state = game.current_state.make_move('ll')
        >>> game.current_state = game.current_state.make_move('ll')
        >>> game.current_state = game.current_state.make_move('rl')
        >>> game.current_state = game.current_state.make_move('lr')
        >>> game.is_winner('p1')
        True
        >>> game.is_winner('p2')
        False
        """
        # Winner only if the other player has no fingers on both hands.
        other = self.current_state.get_other_player(player)
        return (self.current_state.hands[other][LEFT_HAND] == 0
                and self.current_state.hands[other][RIGHT_HAND] == 0)


class CurrentChopsticksState(CurrentState):
    """ The current state class for the Chopsticks game as a subclass from
    the generic current state class.

    current_player - the player currently making a move
    hands - a dictionary containing the current hands of both players
    """

    current_player: str
    hands: Dict[str, List[int]]

    def __init__(self, is_p1_turn: bool) -> None:
        """ Initializes the current state for the Chopsticks class.

        >>> state = CurrentChopsticksState(True)
        >>> state.current_player
        'p1'
        >>> state.hands
        {'p1': [1, 1], 'p2': [1, 1]}
        """
        # Initializes the current player through the generic __init__.
        CurrentState.__init__(self, is_p1_turn)

        # Sets the initial states for the player hands.
        self.hands = {'p1': [1, 1], 'p2': [1, 1]}

    def __str__(self) -> str:
        """ Outputs the string representation of the current chopsticks state.

        >>> state = CurrentChopsticksState(False)
        >>> str(state)
        'Player 1: 1 - 1; Player 2: 1 - 1'
        >>> str(state.make_move('rr'))
        'Player 1: 1 - 2; Player 2: 1 - 1'
        """
        # Builds a str to output the states of the hands in specified format.
        st = ('Player 1: ' + str(self.hands['p1'][LEFT_HAND]) + ' - '
              + str(self.hands['p1'][RIGHT_HAND]) + '; '
              + 'Player 2: ' + str(self.hands['p2'][LEFT_HAND]) + ' - '
              + str(self.hands['p2'][RIGHT_HAND]))
        return st

    def __eq__(self, other: "CurrentChopsticksState") -> bool:
        """ Returns True iff two Game objects are equal by comparing
        the hands of each player for equality, False otherwise.

        >>> state1 = CurrentChopsticksState(False)
        >>> state2 = CurrentChopsticksState(True)
        >>> state1 == state2
        True
        >>> state1 = state1.make_move('rr')
        >>> state1 == state2
        False
        >>> state1 = state1.make_move('lr')
        >>> state2 = state2.make_move('lr')
        >>> state2 = state2.make_move('lr')
        >>> state1 == state2
        True
        """
        # Determines if the two objects are of same type and same hand states.
        return (type(self) == type(other)
                and self.hands['p1'] == other.hands['p1']
                and self.hands['p2'] == other.hands['p2'])

    def get_current_player_name(self) -> str:
        """ Returns who the current player is in the current state of the
        Chopsticks game.

        >>> state = CurrentChopsticksState(False)
        >>> state.get_current_player_name()
        'p2'
        >>> state = state.make_move('rr')
        >>> state.get_current_player_name()
        'p1'
        """
        return self.current_player

    def get_other_player(self, player: str) -> str:
        """ Built in method to get the player who is not currently
        making a move.

        >>> state = CurrentChopsticksState(True)
        >>> state.current_player
        'p1'
        >>> state.get_other_player(state.get_current_player_name())
        'p2'
        """
        # Returns the only other player name as there are two players.
        if player == 'p1':
            return 'p2'
        return 'p1'

    def get_possible_moves(self) -> List[str]:
        """ Returns all possible (legal) moves to be made in the current
        Chopsticks state of the game as either 'rr', 'rl', 'lr', or 'll'.

        >>> state = CurrentChopsticksState(True)
        >>> state.get_possible_moves()
        ['ll', 'lr', 'rl', 'rr']
        >>> state = CurrentChopsticksState(True)
        >>> state.hands['p1'][LEFT_HAND] = 0
        >>> state.get_possible_moves()
        ['rl', 'rr']
        >>> state = CurrentChopsticksState(True)
        >>> state.hands['p1'][RIGHT_HAND] = 0
        >>> state.get_possible_moves()
        ['ll', 'lr']
        >>> state = CurrentChopsticksState(True)
        >>> state.hands['p2'][LEFT_HAND] = 0
        >>> state.get_possible_moves()
        ['lr', 'rr']
        >>> state = CurrentChopsticksState(True)
        >>> state.hands['p2'][RIGHT_HAND] = 0
        >>> state.get_possible_moves()
        ['ll', 'rl']
        >>> state = CurrentChopsticksState(True)
        >>> state.hands['p1'][RIGHT_HAND] = 0
        >>> state.hands['p2'][RIGHT_HAND] = 0
        >>> state.get_possible_moves()
        ['ll']
        >>> state = CurrentChopsticksState(True)
        >>> state.hands['p1'][RIGHT_HAND] = 0
        >>> state.hands['p2'][LEFT_HAND] = 0
        >>> state.get_possible_moves()
        ['lr']
        >>> state = CurrentChopsticksState(True)
        >>> state.hands['p1'][LEFT_HAND] = 0
        >>> state.hands['p2'][RIGHT_HAND] = 0
        >>> state.get_possible_moves()
        ['rl']
        >>> state = CurrentChopsticksState(True)
        >>> state.hands['p1'][LEFT_HAND] = 0
        >>> state.hands['p2'][LEFT_HAND] = 0
        >>> state.get_possible_moves()
        ['rr']
        >>> state = CurrentChopsticksState(False)
        >>> state.get_possible_moves()
        ['ll', 'lr', 'rl', 'rr']
        >>> state = CurrentChopsticksState(False)
        >>> state.hands['p2'][LEFT_HAND] = 0
        >>> state.get_possible_moves()
        ['rl', 'rr']
        >>> state = CurrentChopsticksState(False)
        >>> state.hands['p2'][RIGHT_HAND] = 0
        >>> state.get_possible_moves()
        ['ll', 'lr']
        >>> state = CurrentChopsticksState(False)
        >>> state.hands['p1'][LEFT_HAND] = 0
        >>> state.get_possible_moves()
        ['lr', 'rr']
        >>> state = CurrentChopsticksState(False)
        >>> state.hands['p1'][RIGHT_HAND] = 0
        >>> state.get_possible_moves()
        ['ll', 'rl']
        >>> state = CurrentChopsticksState(False)
        >>> state.hands['p2'][RIGHT_HAND] = 0
        >>> state.hands['p1'][RIGHT_HAND] = 0
        >>> state.get_possible_moves()
        ['ll']
        >>> state = CurrentChopsticksState(False)
        >>> state.hands['p2'][RIGHT_HAND] = 0
        >>> state.hands['p1'][LEFT_HAND] = 0
        >>> state.get_possible_moves()
        ['lr']
        >>> state = CurrentChopsticksState(False)
        >>> state.hands['p2'][LEFT_HAND] = 0
        >>> state.hands['p1'][RIGHT_HAND] = 0
        >>> state.get_possible_moves()
        ['rl']
        >>> state = CurrentChopsticksState(False)
        >>> state.hands['p2'][LEFT_HAND] = 0
        >>> state.hands['p1'][LEFT_HAND] = 0
        >>> state.get_possible_moves()
        ['rr']
        """
        # Builds a list of possible moves by judging if the
        # either the dealing or receiving hand is alive.
        moves = []
        player = self.current_player
        other = self.get_other_player(player)
        if self.hands[player][LEFT_HAND] != 0:
            if self.hands[other][LEFT_HAND] != 0:
                moves.append('ll')
            if self.hands[other][RIGHT_HAND] != 0:
                moves.append('lr')
        if self.hands[player][RIGHT_HAND] != 0:
            if self.hands[other][LEFT_HAND] != 0:
                moves.append('rl')
            if self.hands[other][RIGHT_HAND] != 0:
                moves.append('rr')
        return moves

    def is_valid_move(self, move: str) -> bool:
        """ Returns True iff the given move is a valid move of
        the current Chopsticks state.

        >>> state = CurrentChopsticksState(True)
        >>> state.is_valid_move('rr')
        True
        >>> state.is_valid_move('a')
        False
        """
        # Checks if the move is of valid type, and a listed move.
        return (not isinstance(move, type(None))
                and move in self.get_possible_moves())

    def make_move(self, move: str) -> "CurrentChopsticksState":
        """ Updates the current state of the game by updating the
        player hands according to the move done.

        >>> state = CurrentChopsticksState(True)
        >>> state = state.make_move('rr')
        >>> str(state)
        'Player 1: 1 - 1; Player 2: 1 - 2'
        >>> state = state.make_move('rl')
        >>> str(state)
        'Player 1: 3 - 1; Player 2: 1 - 2'
        >>> state = state.make_move('ll')
        >>> str(state)
        'Player 1: 3 - 1; Player 2: 4 - 2'
        >>> state = state.make_move('rr')
        >>> str(state)
        'Player 1: 3 - 3; Player 2: 4 - 2'
        >>> state = state.make_move('lr')
        >>> str(state)
        'Player 1: 3 - 3; Player 2: 4 - 0'
        """
        # Creates a deep copy of the current state to avoid mutalizing
        # the original hands of the original current state.
        import copy
        new = copy.deepcopy(self)
        player = new.current_player
        other = new.get_other_player(player)  # The player that is not playing.
        # Add the fingers of a dealing hand and receiving hand.
        if move == 'll':
            new.hands[other][LEFT_HAND] = ((new.hands[player][LEFT_HAND] +
                                            new.hands[other][LEFT_HAND]) % 5)
        elif move == 'lr':
            new.hands[other][RIGHT_HAND] = ((new.hands[player][LEFT_HAND] +
                                             new.hands[other][RIGHT_HAND]) % 5)
        elif move == 'rl':
            new.hands[other][LEFT_HAND] = ((new.hands[player][RIGHT_HAND] +
                                            new.hands[other][LEFT_HAND]) % 5)
        elif move == 'rr':
            new.hands[other][RIGHT_HAND] = ((new.hands[player][RIGHT_HAND] +
                                             new.hands[other][RIGHT_HAND]) % 5)
        if new.current_player == 'p1':
            new.current_player = 'p2'
        else:
            new.current_player = 'p1'
        return new


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")

    import doctest
    doctest.testmod()
