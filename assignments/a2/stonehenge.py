"""
Implementation of the StoneHenge game.
"""
from typing import Any, List, Dict
from game import Game
from game_state import GameState


class StonehengeGame(Game):
    """
    The generic class for Stonehenge that is a sub-class of
    the abstract class Game.
    """

    def __init__(self, is_p1_turn: bool, size: int = -1) -> None:
        """
        Initializes the Stonehenge game.

        >>> sh = StonehengeGame(True, 2)
        >>> sh.current_state.size
        2
        >>> sh.current_state.p1_turn
        True
        """
        # Parameter size has a default value where a size can be passed in.
        if size == -1:
            size = None
            while not isinstance(size, int):
                size = int(input('Please enter the size of the board: '))
        # Initializes the game state.
        self.current_state = StonehengeState(is_p1_turn, size)

    def get_instructions(self) -> str:
        """
        Returns a str type of the instructions for the
        Stonehenge game.

        >>> sh = StonehengeGame(True, 5)
        >>> print(sh.get_instructions())
        The Stonehenge Game starts with a hexagonal grid
        of various sizes with the shape of a triangle
        without the corners. Players take turns claiming
        cells on the board and the first to get atleast half
        of the cells in a ley line, claims the ley line!
        The first player to claim at least half of the
        wins the game! Good luck!
        """
        return ("The Stonehenge Game starts with a hexagonal grid\n" +
                "of various sizes with the shape of a triangle\n" +
                "without the corners. Players take turns claiming\n" +
                "cells on the board and the first to get atleast half\n" +
                "of the cells in a ley line, claims the ley line!\n" +
                "The first player to claim at least half of the\n" +
                "wins the game! Good luck!")

    def is_over(self, state: "StonehengeState") -> bool:
        """
        Returns whether the Stonehenge game is over at
        StonehengeState.

        >>> sh1 = StonehengeGame(True, 1)
        >>> sh1.is_over(sh1.current_state)
        False
        >>> sh1.current_state = sh1.current_state.make_move('A')
        >>> sh1.is_over(sh1.current_state)
        True
        >>> sh2 = StonehengeGame(True, 3)
        >>> sh2.current_state = sh2.current_state.make_move('A')
        >>> sh2.current_state = sh2.current_state.make_move('B')
        >>> sh2.current_state = sh2.current_state.make_move('C')
        >>> sh2.current_state = sh2.current_state.make_move('D')
        >>> sh2.current_state = sh2.current_state.make_move('E')
        >>> sh2.current_state = sh2.current_state.make_move('F')
        >>> sh2.current_state = sh2.current_state.make_move('G')
        >>> sh2.current_state = sh2.current_state.make_move('H')
        >>> sh2.is_over(sh2.current_state)
        False
        >>> sh2.current_state = sh2.current_state.make_move('I')
        >>> sh2.is_over(sh2.current_state)
        True
        """
        half = state.ley_lines / 2
        # If all moves are exhausted or atleast one player has won.
        return (state.used_lines['p1'] >= half
                or state.used_lines['p2'] >= half
                or state.get_possible_moves() == [])

    def is_winner(self, player: str) -> bool:
        """
        Returns whether player has won the StonehengeGame.

        >>> sh1 = StonehengeGame(True, 1)
        >>> sh1.current_state = sh1.current_state.make_move('A')
        >>> sh1.is_winner('p1')
        True
        >>> sh2 = StonehengeGame(False, 1)
        >>> sh2.current_state = sh2.current_state.make_move('A')
        >>> sh2.is_winner('p1')
        False
        """
        # Whether the player has half or more of the ley-lines claimed.
        return (self.current_state.used_lines[player] >=
                self.current_state.ley_lines / 2)

    def str_to_move(self, string: str) -> Any:
        """
        Returns the move that the string represents, or
        an invalid move if string is not a move.

        >>> sh1 = StonehengeGame(False, 4)
        >>> sh1.str_to_move('                   g         ')
        'G'
        >>> sh1.str_to_move(' A')
        'A'
        """
        return string.strip().upper()


class StonehengeState(GameState):
    """
    State of the StonehengeGame at a point in time.
    """
    row: List[List[str]]  # Every row ley-line
    d_r: List[List[str]]  # Every down-right diagonal ley-line
    d_l: List[List[str]]  # Every down-left diagonal ley-line
    size: int  # Classification of the order of the board.
    used_lines: Dict[str, int]  # How many ley-lines the players have claimed.
    ley_lines: int  # The number of total ley-lines of the board.

    def __init__(self, is_p1_turn: bool, size: int) -> None:
        """
        Initializes the StoneHengeState class.

        >>> shs = StonehengeState(True, 3)
        >>> shs.p1_turn
        True
        >>> shs.size
        3
        >>> shs.ley_lines
        12
        >>> shs.used_lines
        {'p1': 0, 'p2': 0}
        >>> shs.row[2]
        ['@', 'F', 'G', 'H', 'I']
        """
        # Uses the super class to initialize the player turn.
        GameState.__init__(self, is_p1_turn)
        # Initializes all attributes accordingly.
        self.size = size
        self._get_lines(self.size)
        self.ley_lines = (self.size + 1) * 3
        self.used_lines = {'p1': 0, 'p2': 0}

    def __str__(self) -> str:
        """
        Returns a str representation of the current state of
        the StonehengeGame visually.

        Based on the inability to translate this function's output accordingly,
        Docstrings are not provided.
        """
        # Returns a str type based on the order size.
        if self.size == 1:
            st = ('       {}   {}\n'.format(self.d_l[0][0],
                                            self.d_l[1][0]) +
                  '      /   /\n' +
                  ' {} - {} - {}\n'.format(self.row[0][0],
                                           self.row[0][1],
                                           self.row[0][2]) +
                  '      \\ / \\\n' +
                  '   {} - {}   {}\n'.format(self.row[1][0],
                                             self.row[1][1],
                                             self.d_r[0][0]) +
                  '        \\\n' +
                  '         {}'.format(self.d_r[1][0]))
        elif self.size == 2:
            st = ('        {}   {}\n'.format(self.d_l[0][0],
                                             self.d_l[1][0]) +
                  '       /   /\n' +
                  '  {} - {} - {}   {}\n'.format(self.row[0][0],
                                                 self.row[0][1],
                                                 self.row[0][2],
                                                 self.d_l[2][0]) +
                  '     / \\ / \\ /\n' +
                  '{} - {} - {} - {}\n'.format(self.row[1][0],
                                               self.row[1][1],
                                               self.row[1][2],
                                               self.row[1][3]) +
                  '     \\ / \\ / \\\n' +
                  '  {} - {} - {}   {}\n'.format(self.row[2][0],
                                                 self.row[2][1],
                                                 self.row[2][2],
                                                 self.d_r[1][0]) +
                  '       \\   \\\n' +
                  '        {}   {}'.format(self.d_r[2][0],
                                           self.d_r[0][0]))
        elif self.size == 3:
            st = ('           {}   {}\n'.format(self.d_l[0][0],
                                                self.d_l[1][0]) +
                  '          /   /\n' +
                  '     {} - {} - {}   {}\n'.format(self.row[0][0],
                                                    self.row[0][1],
                                                    self.row[0][2],
                                                    self.d_l[2][0]) +
                  '        / \\ / \\ /\n' +
                  '   {} - {} - {} - {}   {}\n'.format(self.row[1][0],
                                                       self.row[1][1],
                                                       self.row[1][2],
                                                       self.row[1][3],
                                                       self.d_l[3][0]) +
                  '      / \\ / \\ / \\ /\n' +
                  ' {} - {} - {} - {} - {}\n'.format(self.row[2][0],
                                                     self.row[2][1],
                                                     self.row[2][2],
                                                     self.row[2][3],
                                                     self.row[2][4]) +
                  '      \\ / \\ / \\ / \\\n' +
                  '   {} - {} - {} - {}   {}\n'.format(self.row[3][0],
                                                       self.row[3][1],
                                                       self.row[3][2],
                                                       self.row[3][3],
                                                       self.d_r[1][0]) +
                  '        \\   \\   \\\n' +
                  '         {}   {}   {}'.format(self.d_r[3][0],
                                                 self.d_r[2][0],
                                                 self.d_r[0][0]))
        elif self.size == 4:
            st = ('             {}   {}\n'.format(self.d_l[0][0],
                                                  self.d_l[1][0]) +
                  '            /   /\n' +
                  '       {} - {} - {}   {}\n'.format(self.row[0][0],
                                                      self.row[0][1],
                                                      self.row[0][2],
                                                      self.d_l[2][0]) +
                  '          / \\ / \\ /\n' +
                  '     {} - {} - {} - {}   {}\n'.format(self.row[1][0],
                                                         self.row[1][1],
                                                         self.row[1][2],
                                                         self.row[1][3],
                                                         self.d_l[3][0]) +
                  '        / \\ / \\ / \\ /\n' +
                  '   {} - {} - {} - {} - {}   {}\n'.format(self.row[2][0],
                                                            self.row[2][1],
                                                            self.row[2][2],
                                                            self.row[2][3],
                                                            self.row[2][4],
                                                            self.d_l[4][0]) +
                  '      / \\ / \\ / \\ / \\ /\n' +
                  ' {} - {} - {} - {} - {} - {}\n'.format(self.row[3][0],
                                                          self.row[3][1],
                                                          self.row[3][2],
                                                          self.row[3][3],
                                                          self.row[3][4],
                                                          self.row[3][5]) +
                  '      \\ / \\ / \\ / \\ / \\\n' +
                  '   {} - {} - {} - {} - {}   {}\n'.format(self.row[4][0],
                                                            self.row[4][1],
                                                            self.row[4][2],
                                                            self.row[4][3],
                                                            self.row[4][4],
                                                            self.d_r[1][0]) +
                  '        \\   \\   \\   \\\n' +
                  '         {}   {}   {}   {}'.format(self.d_r[4][0],
                                                      self.d_r[3][0],
                                                      self.d_r[2][0],
                                                      self.d_r[0][0]))
        else:
            st = ('               {}   {}\n'.format(self.d_l[0][0],
                                                    self.d_l[1][0]) +
                  '              /   /\n' +
                  '         {} - {} - {}   {}\n'.format(self.row[0][0],
                                                        self.row[0][1],
                                                        self.row[0][2],
                                                        self.d_l[2][0]) +
                  '            / \\ / \\ /\n' +
                  '       {} - {} - {} - {}   {}\n'.format(self.row[1][0],
                                                           self.row[1][1],
                                                           self.row[1][2],
                                                           self.row[1][3],
                                                           self.d_l[3][0]) +
                  '          / \\ / \\ / \\ /\n' +
                  '     {} - {} - {} - {} - {}   {}\n'.format(self.row[2][0],
                                                              self.row[2][1],
                                                              self.row[2][2],
                                                              self.row[2][3],
                                                              self.row[2][4],
                                                              self.d_l[4][0]) +
                  '        / \\ / \\ / \\ / \\ /\n' +
                  '   {} - {} - {} - {} - {} - {}   {}\n'.format(self.row[3][0],
                                                                 self.row[3][1],
                                                                 self.row[3][2],
                                                                 self.row[3][3],
                                                                 self.row[3][4],
                                                                 self.row[3][5],
                                                                 self.d_l[5][0])
                  + '      / \\ / \\ / \\ / \\ / \\ /\n' +
                  ' {} - {} - {} - {} - {} - {} - {}\n'.format(self.row[4][0],
                                                               self.row[4][1],
                                                               self.row[4][2],
                                                               self.row[4][3],
                                                               self.row[4][4],
                                                               self.row[4][5],
                                                               self.row[4][6]) +
                  '      \\ / \\ / \\ / \\ / \\ / \\\n' +
                  '   {} - {} - {} - {} - {} - {}   {}\n'.format(self.row[5][0],
                                                                 self.row[5][1],
                                                                 self.row[5][2],
                                                                 self.row[5][3],
                                                                 self.row[5][4],
                                                                 self.row[5][5],
                                                                 self.d_r[1][0])
                  + '        \\   \\   \\   \\   \\\n' +
                  '         {}   {}   {}   {}   {}'.format(self.d_r[5][0],
                                                           self.d_r[4][0],
                                                           self.d_r[3][0],
                                                           self.d_r[2][0],
                                                           self.d_r[0][0]))
        return st

    def __repr__(self) -> str:
        """
        Returns a str representation of the object of the
        StonehengeGame.

        >>> sh1 = StonehengeGame(False, 2)
        >>> sh1.current_state = sh1.current_state.make_move('D')
        >>> sh1.current_state = sh1.current_state.make_move('A')
        >>> sh1.current_state = sh1.current_state.make_move('B')
        >>> sh1.current_state = sh1.current_state.make_move('E')
        >>> print(sh1.current_state.__repr__())
        Current Player: p2, Player 1: 3 ley line(s), Player 2: 2 ley line(s).
        >>> sh2 = StonehengeGame(True, 3)
        >>> sh2.current_state = sh2.current_state.make_move('A')
        >>> sh2.current_state = sh2.current_state.make_move('B')
        >>> sh2.current_state = sh2.current_state.make_move('C')
        >>> sh2.current_state = sh2.current_state.make_move('D')
        >>> sh2.current_state = sh2.current_state.make_move('E')
        >>> sh2.current_state = sh2.current_state.make_move('F')
        >>> sh2.current_state = sh2.current_state.make_move('G')
        >>> sh2.current_state = sh2.current_state.make_move('H')
        >>> print(sh2.current_state.__repr__())
        Current Player: p1, Player 1: 4 ley line(s), Player 2: 4 ley line(s).
        """
        # Returns only basic information about the current game state.
        s = ("Current Player: " + self.get_current_player_name() + ", " +
             "Player 1: {} ley line(s), Player 2: {} ley line(s).")
        return s.format(self.used_lines['p1'], self.used_lines['p2'])

    def get_possible_moves(self) -> list:
        """
        Returns a list of all possible moves that can be
        made in the given StonehengeState.

        >>> sh1 = StonehengeGame(False, 2)
        >>> sh1.current_state = sh1.current_state.make_move('D')
        >>> sh1.current_state = sh1.current_state.make_move('A')
        >>> sh1.current_state = sh1.current_state.make_move('B')
        >>> sh1.current_state = sh1.current_state.make_move('E')
        >>> sh1.current_state.get_possible_moves()
        ['C', 'F', 'G']
        >>> sh2 = StonehengeGame(True, 1)
        >>> sh2.current_state.get_possible_moves()
        ['A', 'B', 'C']
        >>> sh2.current_state = sh2.current_state.make_move('B')
        >>> sh2.current_state.get_possible_moves()
        []
        """
        moves = []

        # If the game state is over, there should be no 'possible' moves.
        if ((self.used_lines['p1'] >= self.ley_lines / 2
             or self.used_lines['p2'] >= self.ley_lines / 2)):
            return moves

        # Compiles all letters in rows into a list.
        for ley_line in self.row:
            for element in ley_line:
                if element.isalpha():
                    moves.append(element)
        # Compiles all letters in diagonal lefts into a list.
        for ley_line in self.d_l:
            for element in ley_line:
                if element.isalpha():
                    moves.append(element)
        # Compiles all letters in diagonal rights into a list.
        for ley_line in self.d_r:
            for element in ley_line:
                if element.isalpha():
                    moves.append(element)
        # Eliminates all repeats and returns a sorted list.
        moves = list(set(moves))
        moves.sort()
        return moves

    def get_current_player_name(self) -> str:
        """
        Returns the current player of the StoneHengeState
        as 'p1' or 'p2'. (Directly inherits from the super class).

        >>> sh1 = StonehengeState(True, 2)
        >>> sh1.get_current_player_name()
        'p1'
        >>> sh1.make_move('A').get_current_player_name()
        'p2'
        """
        # Directly uses the super class to find the player name.
        return GameState.get_current_player_name(self)

    def make_move(self, move: str) -> "StonehengeState":
        """
        Returns the new StonehengeState with the move applied.

        >>> sh = StonehengeState(False, 3)
        >>> sh.get_current_player_name()
        'p2'
        >>> sh.get_possible_moves()
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
        >>> sh.used_lines
        {'p1': 0, 'p2': 0}
        >>> new = sh.make_move('B')
        >>> new.get_current_player_name()
        'p1'
        >>> new.get_possible_moves()
        ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
        >>> new.used_lines
        {'p1': 0, 'p2': 1}
        """
        # Creates a copy to avoid causing mutability of the state.
        import copy
        new = copy.deepcopy(self)
        player = new.get_current_player_name()[-1]
        # Goes through each row and replaces the letters with the player move.
        for ley in range(len(new.row)):
            for i in range(len(new.row[ley])):
                if new.row[ley][i] == move:
                    new.row[ley][i] = player
            if ((new.row[ley].count(player) >=
                 (len(new.row[ley]) - 1) / 2 and new.row[ley][0] == '@')):
                new.row[ley][0] = player
                new.used_lines[new.get_current_player_name()] += 1
        # Goes through each diagonal left and replaces the letters with move.
        for ley in range(len(new.d_l)):
            for i in range(len(new.d_l[ley])):
                if new.d_l[ley][i] == move:
                    new.d_l[ley][i] = player
            if ((new.d_l[ley].count(player) >=
                 (len(new.d_l[ley]) - 1) / 2 and new.d_l[ley][0] == '@')):
                new.d_l[ley][0] = player
                new.used_lines[new.get_current_player_name()] += 1
        # Goes through each diagonal right and replaces the letters with move.
        for ley in range(len(new.d_r)):
            for i in range(len(new.d_r[ley])):
                if new.d_r[ley][i] == move:
                    new.d_r[ley][i] = player
            if ((new.d_r[ley].count(player) >=
                 (len(new.d_r[ley]) - 1) / 2 and new.d_r[ley][0] == '@')):
                new.d_r[ley][0] = player
                new.used_lines[new.get_current_player_name()] += 1
        # Alternates the player turn to the other player and returns the copy.
        new.p1_turn = False if new.p1_turn else True
        return new

    def is_valid_move(self, move: Any) -> bool:
        """
        Returns if the move given is valid for the state.

        >>> sh = StonehengeState(True, 1)
        >>> sh.is_valid_move('  a   ')
        False
        >>> sh.is_valid_move('A')
        True
        """
        # Inherits from the super class directly.
        return GameState.is_valid_move(self, move)

    def rough_outcome(self) -> float:
        """
        Returns an estimated interval [LOSE, WIN] of the best
        outcome the current player can get from the state.

        >>> sh = StonehengeGame(True, 2)
        >>> sh.current_state = sh.current_state.make_move('A')
        >>> sh.current_state.rough_outcome()
        0
        >>> sh.current_state = sh.current_state.make_move('E')
        >>> sh.current_state.rough_outcome()
        0
        >>> other = sh.current_state.make_move('F')
        >>> other.rough_outcome()
        -1
        >>> sh.current_state = sh.current_state.make_move('B')
        >>> sh.current_state.rough_outcome()
        0
        >>> sh.current_state = sh.current_state.make_move('F')
        >>> sh.current_state.rough_outcome()
        -1
        >>> sh.current_state = sh.current_state.make_move('D')
        >>> sh.current_state.rough_outcome()
        1
        >>> sh.current_state = sh.current_state.make_move('F')
        >>> sh.current_state.rough_outcome()
        1
        """
        player = self.get_current_player_name()

        # Case 0: the game is already over.
        if self.used_lines[player] >= self.ley_lines / 2:
            return self.WIN
        elif (self.used_lines[player] >= self.ley_lines / 2
              or self.get_possible_moves() == []):
            return self.LOSE
        # Case 1: There is one move that wins it for the current payer.
        l = []
        for move in self.get_possible_moves():
            l.append(self.make_move(move))
        for state in l:
            if state.used_lines[player] >= state.ley_lines / 2:
                return self.WIN

        # Case 2: Every move ahead results in the other player winning.
        for state in l:
            draw = True
            for next_move in state.get_possible_moves():
                next_state = state.make_move(next_move)
                if ((next_state.used_lines[state.get_current_player_name()]
                     >= next_state.ley_lines / 2)):
                    draw = False
            if draw:
                return self.DRAW
        # Otherwise Case 3: There are no moves to make the player win.
        return self.LOSE

    def _get_lines(self, size: int):
        # Private method that returns a valid translation of
        # the board based on a given size.
        ley = {}
        if size == 1:
            self.row = [['@', 'A', 'B'],
                        ['@', 'C']]
            self.d_r = [['@', 'B'],
                        ['@', 'A', 'C']]
            self.d_l = [['@', 'A'],
                        ['@', 'B', 'C']]
        elif size == 2:
            self.row = [['@', 'A', 'B'],
                        ['@', 'C', 'D', 'E'],
                        ['@', 'F', 'G']]
            self.d_r = [['@', 'A', 'D', 'G'],
                        ['@', 'B', 'E'],
                        ['@', 'C', 'F']]
            self.d_l = [['@', 'A', 'C'],
                        ['@', 'B', 'D', 'F'],
                        ['@', 'E', 'G']]
        elif size == 3:
            self.row = [['@', 'A', 'B'],
                        ['@', 'C', 'D', 'E'],
                        ['@', 'F', 'G', 'H', 'I'],
                        ['@', 'J', 'K', 'L']]
            self.d_r = [['@', 'A', 'D', 'H', 'L'],
                        ['@', 'B', 'E', 'I'],
                        ['@', 'C', 'G', 'K'],
                        ['@', 'F', 'J']]
            self.d_l = [['@', 'A', 'C', 'F'],
                        ['@', 'B', 'D', 'G', 'J'],
                        ['@', 'E', 'H', 'K'],
                        ['@', 'I', 'L']]
        elif size == 4:
            self.row = [['@', 'A', 'B'],
                        ['@', 'C', 'D', 'E'],
                        ['@', 'F', 'G', 'H', 'I'],
                        ['@', 'J', 'K', 'L', 'M', 'N'],
                        ['@', 'O', 'P', 'Q', 'R']]
            self.d_r = [['@', 'A', 'D', 'H', 'M', 'R'],
                        ['@', 'B', 'E', 'I', 'N'],
                        ['@', 'C', 'G', 'L', 'Q'],
                        ['@', 'F', 'K', 'P'],
                        ['@', 'J', 'O']]
            self.d_l = [['@', 'A', 'C', 'F', 'J'],
                        ['@', 'B', 'D', 'G', 'K', 'O'],
                        ['@', 'E', 'H', 'L', 'P'],
                        ['@', 'I', 'M', 'Q'],
                        ['@', 'N', 'R']]
        else:
            self.row = [['@', 'A', 'B'],
                        ['@', 'C', 'D', 'E'],
                        ['@', 'F', 'G', 'H', 'I'],
                        ['@', 'J', 'K', 'L', 'M', 'N'],
                        ['@', 'O', 'P', 'Q', 'R', 'S', 'T'],
                        ['@', 'U', 'V', 'W', 'X', 'Y']]
            self.d_r = [['@', 'A', 'D', 'H', 'M', 'S', 'Y'],
                        ['@', 'B', 'E', 'I', 'N', 'T'],
                        ['@', 'C', 'G', 'L', 'R', 'X'],
                        ['@', 'F', 'K', 'Q', 'W'],
                        ['@', 'J', 'P', 'V'],
                        ['@', 'O', 'U']]
            self.d_l = [['@', 'A', 'C', 'F', 'J', 'O'],
                        ['@', 'B', 'D', 'G', 'K', 'P', 'U'],
                        ['@', 'E', 'H', 'L', 'Q', 'V'],
                        ['@', 'I', 'M', 'R', 'W'],
                        ['@', 'N', 'S', 'X'],
                        ['@', 'T', 'Y']]
        return ley


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
