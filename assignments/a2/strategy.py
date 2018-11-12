"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any, List
import copy
from game import Game


# Added the Tree class as done in class for use in the minimax strategies.
class Tree:
    """
    Represents a basic (initialized) Tree object
    """

    def __init__(self, value: object = None,
                 children: List['Tree'] = None) -> None:
        """ Initializes the Tree object with a value, children, and score.
        """
        self.value = value
        self.children = children[:] if children is not None else []
        self.score = None


# Added the Stack class as done in class for use in the minimax strategies.
class Stack:
    """
    Last-in, first-out (LIFO) stack.
    """

    _contents: list

    def __init__(self) -> None:
        """
        Create a new, empty Stack self.

        >>> s = Stack()
        """
        self._contents = []  # Private attribute should not be accessed directy

    def add(self, obj: object) -> None:
        """
        Add object obj to top of Stack self.

        >>> s = Stack()
        >>> s.add(7)
        """
        self._contents.append(obj)

    def remove(self) -> object:
        """
        Remove and return top element of Stack self.
        Assume Stack self is not empty.

        >>> s = Stack()
        >>> s.add(5)
        >>> s.add(7)
        >>> s.remove()
        7
        """
        return self._contents.pop()

    def is_empty(self) -> bool:
        """
        Return whether Stack self is empty.

        >>> s = Stack()
        >>> s.is_empty()
        True
        >>> s.add(7)
        >>> s.is_empty()
        False
        """
        return len(self._contents) == 0


def interactive_strategy(game: Game) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily - just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move


def recursive_minimax_strategy(game: Any) -> Any:
    """ Returns a move by searching through ever possible
    path the game can take recursively.

    >>> from stonehenge import StonehengeGame
    >>> s = StonehengeGame(True, 2)
    >>> s.current_state = s.current_state.make_move('C')
    >>> s.current_state = s.current_state.make_move('B')
    >>> s.current_state = s.current_state.make_move('D')
    >>> s.current_state = s.current_state.make_move('F')
    >>> recursive_minimax_strategy(s)
    'E'
    >>> s = StonehengeGame(True, 2)
    >>> s.current_state = s.current_state.make_move('C')
    >>> recursive_minimax_strategy(s)
    'A'
    >>> s = StonehengeGame(True, 1)
    >>> recursive_minimax_strategy(s)
    'A'
    >>> s = StonehengeGame(True, 2)
    >>> s.current_state = s.current_state.make_move('A')
    >>> s.current_state = s.current_state.make_move('F')
    >>> s.current_state = s.current_state.make_move('D')
    >>> recursive_minimax_strategy(s)
    'E'
    """
    # Gets all the moves and states
    possible_moves = game.current_state.get_possible_moves()
    possible_games = []
    # Apply every move and add each game copy to a list.
    for move in possible_moves:
        possible_game = copy.deepcopy(game)
        new_state = possible_game.current_state.make_move(move)
        possible_game.current_state = new_state
        possible_games.append(possible_game)
    # Recursively go through each game to find its best score.
    possible_scores = [-1 * recursive_minimax_get_score(g)
                       for g in possible_games]
    # Returns in precedent order, the first win, draw, or loss.
    if 1 in possible_scores:
        return possible_moves[possible_scores.index(1)]
    elif 0 in possible_scores:
        return possible_moves[possible_scores.index(0)]
    return possible_moves[possible_scores.index(-1)]


def recursive_minimax_get_score(game: Any) -> int:
    """ Used to get the best score of each specified game
    by recursively searching through every possible path.

    >>> from stonehenge import StonehengeGame
    >>> s = StonehengeGame(True, 2)
    >>> s.current_state = s.current_state.make_move('C')
    >>> s.current_state = s.current_state.make_move('B')
    >>> s.current_state = s.current_state.make_move('D')
    >>> s.current_state = s.current_state.make_move('F')
    >>> recursive_minimax_get_score(s)
    1
    >>> s = StonehengeGame(True, 2)
    >>> s.current_state = s.current_state.make_move('C')
    >>> recursive_minimax_get_score(s)
    -1
    >>> s = StonehengeGame(True, 1)
    >>> recursive_minimax_get_score(s)
    1
    >>> s = StonehengeGame(True, 2)
    >>> s.current_state = s.current_state.make_move('A')
    >>> s.current_state = s.current_state.make_move('F')
    >>> s.current_state = s.current_state.make_move('D')
    >>> recursive_minimax_get_score(s)
    1
    """
    # Base case: The game is over. Return who won as 1, 0, or -1
    if game.is_over(game.current_state):
        current_player = game.current_state.get_current_player_name()
        other_player = 'p2' if current_player == 'p1' else 'p1'
        if game.is_winner(current_player):
            return 1
        elif game.is_winner(other_player):
            return -1
        return 0
    # Recursive step: Search through the next games.
    else:
        possible_games = []
        # Go through each move and call the function again.
        for move in game.current_state.get_possible_moves():
            possible_game = copy.deepcopy(game)
            new_state = possible_game.current_state.make_move(move)
            possible_game.current_state = new_state
            possible_games.append(possible_game)
        # Get the best score and return it.
        return max([recursive_minimax_get_score(g) * -1
                    for g in possible_games])


def iterative_minimax_strategy(game: Any) -> Any:
    """ Returns a move by searching through every path the
    game can take in an iterative fashion using Stacks.

    >>> from stonehenge import StonehengeGame
    >>> s = StonehengeGame(True, 2)
    >>> s.current_state = s.current_state.make_move('C')
    >>> s.current_state = s.current_state.make_move('B')
    >>> s.current_state = s.current_state.make_move('D')
    >>> s.current_state = s.current_state.make_move('F')
    >>> iterative_minimax_strategy(s)
    'E'
    >>> s = StonehengeGame(True, 2)
    >>> s.current_state = s.current_state.make_move('C')
    >>> iterative_minimax_strategy(s)
    'A'
    >>> s = StonehengeGame(True, 1)
    >>> iterative_minimax_strategy(s)
    'A'
    >>> s = StonehengeGame(True, 2)
    >>> s.current_state = s.current_state.make_move('A')
    >>> s.current_state = s.current_state.make_move('F')
    >>> s.current_state = s.current_state.make_move('D')
    >>> iterative_minimax_strategy(s)
    'E'
    """
    possible_moves = game.current_state.get_possible_moves()
    # Initializes the stack and puts the first value into it.
    stack = Stack()
    stack.add(Tree(game.current_state))
    state_node = Tree()
    # Keep looking through every state until there are none to look at.
    while not stack.is_empty():
        # Removes the last (added) item from the stack.
        state_node = stack.remove()
        # Case 1: The state is over, assign a score.
        if state_node.value.get_possible_moves() == []:
            copy_game = copy.deepcopy(game)
            copy_game.current_state = state_node.value
            current_player = state_node.value.get_current_player_name()
            other_player = 'p2' if current_player == 'p1' else 'p1'
            if copy_game.is_winner(current_player):
                state_node.score = 1
            elif copy_game.is_winner(other_player):
                state_node.score = -1
            else:
                state_node.score = 0
        # Case 2: The state has children already acted upon.
        elif state_node.children != []:
            # Return a valid score based on its children.
            state_node.score = max([child.score * -1
                                    for child in state_node.children])
        # Case 3: The state has unacted upon children.
        else:
            # Act on the node's children
            copy_state = state_node.value
            state_node.children = [Tree(state_node.value.make_move(move))
                                   for move in copy_state.get_possible_moves()]
            # Add itself and its children back to the stack.
            stack.add(state_node)
            for child in state_node.children:
                stack.add(child)
    scores = [child.score * -1 for child in state_node.children]
    # Return the best move from scores among all of its children.
    return possible_moves[scores.index(state_node.score)]

if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
