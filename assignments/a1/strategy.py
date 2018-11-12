"""
Lists the strategies that a computer can use for an arbitrary game.
"""
from typing import Any
from random import randint
from game import Game


def interactive_strategy(game: Game) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def random_strategy(game: Game) -> Any:
    """
    Return a move for the game randomly among the possible legal moves.
    """
    # Returns an item based on a randomly generated number.
    possible_moves = game.current_state.get_possible_moves()
    return possible_moves[randint(0, len(possible_moves) - 1)]


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
