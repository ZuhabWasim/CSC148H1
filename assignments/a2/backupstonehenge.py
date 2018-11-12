"""
Implementation of the StoneHenge game.
"""
from typing import Any, Dict, List
from game import Game
from game_state import GameState


class StonehengeGame(Game):
    """
    The generic class for Stonehenge that is a sub-class of
    the abstract class Game.
    """

    def __init__(self, is_p1_turn: bool) -> None:
        """
        Initializes the Stonehenge game.
        """
        self.current_state = StonehengeState(is_p1_turn)

    def get_instructions(self) -> str:
        """
        Returns a str type of the instructions for the
        Stonehenge game.
        """
        return ("The Stonehenge Game starts with a hexagonal grid\n" +
                "of various sizes with the shape of a triangle\n" +
                "without the corners. Players take turns claiming\n" +
                "cells on the board and the first to get atleast half\n" +
                "of the cells in a ley line, claims the ley line!\n" +
                "The first player to claim at least half of the\n" +
                "wins the game! Good luck!")

    def is_over(self, state: "StonehengeGame") -> bool:
        """
        Returns whether the Stonehenge game is over at
        StonehengeState.
        """
        pass

    def is_winner(self, player: str) -> bool:
        """
        Returns whether player has won the StonehengeGame
        """
        pass

    def str_to_move(self, string: str) -> Any:
        """
        Returns the move that the string represents, or
        an invalid move if string is not a move.
        """
        return string.strip().upper()


class StonehengeState(GameState):
    """
    State of the StonehengeGame at a point in time.
    """
    ley_lines: Dict[str, List[List[str]]]
    size: int

    def __init__(self, is_p1_turn: bool) -> None:
        """
        Initializes the StoneHengeState class.
        """
        super().__init__(is_p1_turn)
        self.size = int(input('Enter the size of the board: '))
        self.ley_lines = self._get_ley_lines(self.size)

    def __str__(self) -> str:
        """
        Returns a str representation of the current state of
        the StonehengeGame visually.
        """
        if self.size == 2:
            st = ('        {}   {}\n'.format(self.ley_lines['d_l'][0][0],
                                             self.ley_lines['d_l'][1][0]) +
                  '       /   /\n' +
                  '  {} - {} - {}   {}\n'.format(self.ley_lines['row'][0][0],
                                                 self.ley_lines['row'][0][1],
                                                 self.ley_lines['row'][0][2],
                                                 self.ley_lines['d_l'][2][0]) +
                  '     / \\ / \\ /\n' +
                  '{} - {} - {} - {}\n'.format(self.ley_lines['row'][1][0],
                                               self.ley_lines['row'][1][1],
                                               self.ley_lines['row'][1][2],
                                               self.ley_lines['row'][1][3]) +
                  '     \\ / \\ / \\\n' +
                  '  {} - {} - {}   {}\n'.format(self.ley_lines['row'][2][0],
                                                 self.ley_lines['row'][2][1],
                                                 self.ley_lines['row'][2][2],
                                                 self.ley_lines['d_r'][1][0]) +
                  '       \\   \\\n' +
                  '        {}   {}\n'.format(self.ley_lines['d_r'][2][0],
                                             self.ley_lines['d_r'][0][0]))
            return st
        elif self.size == 3:
            pass
        elif self.size == 4:
            pass
        else:
            pass
        return ''

    def __repr__(self) -> str:
        """
        Returns a str representation of the object of the
        StonehengeGame.
        """
        pass

    def get_possible_moves(self) -> list:
        """
        Returns a list of all possible moves that can be
        made in the given StonehengeState.
        """
        moves = []
        for ley_line_set in self.ley_lines:
            for ley_line in ley_line_set:
                for element in ley_line:
                    if element.isalpha():
                        moves.append(element)
        moves = list(set(moves))
        moves.sort()
        return moves

    def get_current_player_name(self) -> str:
        """
        Returns the current player of the StoneHengeState
        as 'p1' or 'p2'. (Directly inherits from the super class)."""
        return GameState.get_current_player_name(self)

    def make_move(self, move: str) -> "StonehengeState":
        """
        Returns the new StonehengeState with the move applied.
        """
        import copy
        new = copy.deepcopy(self)
        player = new.get_current_player_name()[-1]
        for ley_line_set in new.ley_lines:
            for ley_line in range(ley_line_set):
                for i in range(new.ley_lines[ley_line_set][ley_line]):
                    if new.ley_lines[ley_line_set][ley_line][i] == move:
                        new.ley_lines[ley_line_set][ley_line][i] = move
                if (new.ley_lines[ley_line_set][ley_line].count(move) >=
                        (len(new.ley_lines[ley_line_set][ley_line]) - 1) / 2):
                    new.ley_lines[ley_line_set][ley_line][0] = player
        return new

    def is_valid_move(self, move: Any) -> bool:
        """
        Returns if the move given is valid for the state.
        """
        return GameState.is_valid_move(self, move)

    def rough_outcome(self) -> float:
        """
        Returns an estimated interval [LOSE, WIN] of the best
        outcome the current player can get from the state.
        """
        pass

    def _get_ley_lines(self, size: int):
        # Private method that returns a valid translation of
        # the board based on a given size.
        ley = {}
        if size == 2:
            ley['row'] = [['@', 'A', 'B'],
                          ['@', 'C', 'D', 'E'],
                          ['@', 'F', 'G']]
            ley['d_r'] = [['@', 'A', 'D', 'G'],
                          ['@', 'B', 'E'],
                          ['@', 'C', 'F']]
            ley['d_l'] = [['@', 'A', 'C'],
                          ['@', 'B', 'D', 'F'],
                          ['@', 'E', 'G']]
        elif size == 3:
            pass
        elif size == 4:
            pass
        else:
            pass
        return ley


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
