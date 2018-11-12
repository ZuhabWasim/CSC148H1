"""
Implementation of the Quell game from Steam.
"""
from typing import Any, List
from game import Game
from game_state import GameState

"""
Quell Game Legend:
B - Block
Q - Quell Drop
P - Pearls
  - Empty Space (Space character)
O - Level Border

S - (Seeded) vine
G - (Grown) vine
M - Male block
F - Female block
X - Hoop Entrance
Y - Hoop Exit

K - KLever for spikes
U - Up (facing) spike
D - Down (facing) spike
L - Left (facing) spike
R - Right (facing) spike
A - All (faces) spike

Example Level:
5 - Minimum Moves the level takes
OOOOOOOOOOOOO
OOOB BBBBBOOO
OOB    P  BOO
OB P Q   PBBO
OOB    PB BOO
OOOB B B BOOO
OOOOOOOOOOOOO
"""


class QuellGame(Game):
    """
    The generic class for Quell that is a sub-class of
    the abstract class Game.
    """

    def __init__(self, is_p1_turn: bool, level: str = '') -> None:
        """
        Initializes the Quell game.

        >>> q = QuellGame(True, 'quell_example.txt')
        >>> type(q)
        <class 'quell.QuellGame'>
        """
        # Parameter size has a default value where a size can be passed in.
        if level == '':
            # level = None
            # while not isinstance(level, str):
            #     size = int(input('Please enter the size of the board: '))
            level = input('Please enter a valid text file containing a level: ')

        # Initializes the game state.
        self.current_state = QuellState(is_p1_turn if is_p1_turn else not is_p1_turn, level)

    def get_instructions(self) -> str:
        """
        Returns a str type of the instructions for the
        Stonehenge game.

        >>> sh = QuellGame(True, 'quell_example.txt')
        >>> print(sh.get_instructions())
        The Quell game is lit
        """
        return "The Quell game is lit"

    def is_over(self, state: "QuellState") -> bool:
        """
        Returns whether the Stonehenge game is over at
        QuellState.
        """

    def is_winner(self, player: str) -> bool:
        """
        Returns whether player has won the QuellGame.
        """

    def str_to_move(self, string: str) -> Any:
        """
        Returns the move that the string represents, or
        an invalid move if string is not a move.
        """
        return string.strip().upper()


class QuellState(GameState):
    """
    State of the QuellGame at a point in time.
    """
    useless: bool  # To get pycharm to shut up.

    original_board: List[List[str]]  # The original starting game board.
    current_board: List[List[str]]  # The current (to be altered) board.

    num_moves_made: int  # Number of moves already made.
    num_pearls_got: int  # Number of pearls gotten.

    quell_pos_r: int  # Horizontal position of Quell.
    quell_pos_c: int  # Vertical position of Quell.

    minimum_moves: int  # The minimum moves to beat a level.
    total_pearls: int  # The total pearls available in a level.

    dim_row: int  # The lateral dimension of the level.
    dim_col: int  # The longitudinal dimension of the level.

    def __init__(self, is_p1_turn: bool, level_name: str) -> None:
        """
        Initializes the QuellState class.
        """
        self.useless = is_p1_turn
        level = open(level_name, "r")

        self.minimum_moves = int(level.readline())
        self.num_moves_made = 0
        self.num_pearls_got = 0
        self.total_pearls = 0

        lines = level.readlines()
        self.dim_row = len(lines)
        self.dim_col = len(lines[0].strip())

        self.original_board = []
        self.current_board = []
        for row in range(self.dim_row):
            for col in range(self.dim_col):
                # self.original_board[row][col] = lines[row][col]
                # self.current_board[row][col] = lines[row][col]
                if lines[row].strip()[col] == 'Q':
                    self.quell_pos_r = row
                    self.quell_pos_c = col
                elif lines[row].strip()[col] == 'P':
                    self.total_pearls += 1
            self.original_board.append(list(lines[row].strip()))
            self.current_board.append(list(lines[row].strip()))

    def __str__(self) -> str:
        """
        Returns a str representation of the current state of
        the QuellGame visually.

        Based on the inability to translate this function's output accordingly,
        Docstrings are not provided.

        >>> q = QuellGame(True, 'quell_example.txt')
        >>> print(q.current_state)
        OOOOOOOOOOOOO
        OOOB BBBBBOOO
        OOB    P  BOO
        OB P Q   PBBO
        OOB    PB BOO
        OOOB B B BOOO
        OOOOOOOOOOOOO
        <BLANKLINE>
        Number of moves made:        0
        Minimum moves to beat level: 5
        <BLANKLINE>
        Number of pearls gotten:     0
        Total pearls in level:       4
        <BLANKLINE>
        Quell is at position (3,5) of a 7x13 board.
        """
        st = ''

        for row in range(len(self.current_board)):
            for col in range(len(self.current_board[0])):
                st += self.current_board[row][col]
            st += '\n'

        st += '\nNumber of moves made:        ' + str(self.num_moves_made) + '\n'
        st += 'Minimum moves to beat level: ' + str(self.minimum_moves) + '\n\n'
        st += 'Number of pearls gotten:     ' + str(self.num_pearls_got) + '\n'
        st += 'Total pearls in level:       ' + str(self.total_pearls) + '\n\n'
        st += 'Quell is at position ({0},{1}) of a {2}x{3} board.'.format(
            self.quell_pos_r, self.quell_pos_c, self.dim_row, self.dim_col)

        return st

    def __repr__(self) -> str:
        """
        Returns a str representation of the object of the
        QuellGame.

        """

    def get_possible_moves(self) -> list:
        """
        Returns a list of all possible moves that can be
        made in the given QuellState.
        """

        moves = []
        if self.current_board[self.quell_pos_r - 1][self.quell_pos_c] in [' ', 'K', 'P', 'S']:
            moves.append('U')
        if self.current_board[self.quell_pos_r + 1][self.quell_pos_c] in [' ', 'K', 'P', 'S']:
            moves.append('D')
        if self.current_board[self.quell_pos_r][self.quell_pos_c - 1] in [' ', 'K', 'P', 'S']:
            moves.append('L')
        if self.current_board[self.quell_pos_r][self.quell_pos_c + 1] in [' ', 'K', 'P', 'S']:
            moves.append('R')
        return moves

    def get_current_player_name(self) -> str:
        """
        Returns the current player of the StoneHengeState
        as 'p1' or 'p2'. (Directly inherits from the super class).
        """
        # Directly uses the super class to find the player name.
        return "p1"

    def make_move(self, move: str) -> "QuellState":
        """
        Returns the new QuellState with the move applied.
        """
        from copy import deepcopy
        copy = deepcopy(self)

        copy.num_moves_made += 1
        if copy.num_moves_made >
        if move == 'U':
            og_row = copy.quell_pos_r
            while copy.current_board[copy.quell_pos_r - 1][copy.quell_pos_c] in [' ', 'K', 'P', 'S']:
                copy.quell_pos_r -= 1
                if copy.current_board[copy.quell_pos_r - 1][copy.quell_pos_c] == 'P':
                    copy.num_pearls_got += 1
                    copy.current_board[copy.quell_pos_r - 1][copy.quell_pos_c] = ' '
                elif copy.current_board[copy.quell_pos_r - 1][copy.quell_pos_c] == 'S':
                    copy.current_board[copy.quell_pos_r - 1][copy.quell_pos_c] = 'G'


    def is_valid_move(self, move: Any) -> bool:
        """
        Returns if the move given is valid for the state.

        """
        # Inherits from the super class directly.
        return GameState.is_valid_move(self, move)

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        """
        raise NotImplementedError

if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
