"""
CSC148 - Lab 1 Exercise
"""
from typing import List, Any

UNDER20 = 'under20'
UNDER30 = 'under30'
UNDER40 = 'under40'
ABOVE40 = 'above40'


class RaceRegistry:
    """Represents a registry for organizing a 5k running race
    by categories.

    registry - A dictionary of all racer emails in corresponding speed.

    >>> new_race = RaceRegistry()
    >>> new_race.get_above40()
    []
    >>> new_race.add_runner('gerhard@mail.utoronto.ca', ABOVE40)
    >>> new_race.get_above40()
    ['gerhard@mail.utoronto.ca']
    """

    def __init__(self):
        """Initializes self by creating default empty values for
        future use.

        >>> new_race = RaceRegistry()
        >>> new_race.get_under20()
        []
        >>> new_race.get_under30()
        []
        >>> new_race.get_under40()
        []
        >>> new_race.get_above40()
        []
        """
        self.registry = {'under20': [], 'under30': [], 'under40': [], 'above40': []}

    def add_runner(self, runner_email: str, category: str) -> None:
        """Adds the runner_email in the in the specified category iff the runner
        is not in the registry. If the runner is in the registry, their time gets updated.

        >>> new_race = RaceRegistry()
        >>> new_race.add_runner('toni@mail.utoronto.ca', UNDER20)
        >>> new_race.get_under20()
        ['toni@mail.utoronto.ca']
        >>> new_race.add_runner('toni@mail.utoronto.ca', UNDER40)
        >>> new_race.get_under20()
        []
        >>> new_race.get_under40()
        ['toni@mail.utoronto.ca']
        """
        # Remove the previous recording under the email, if it exists.
        found = ''

        for group in self.registry:
            if runner_email in self.registry[group]:
                found = group

        if found != '':
            self.registry[found].remove(runner_email)

        # Adds (or updates) a new email under a speed category.
        self.registry[category].append(runner_email)

    def get_under20(self) -> List[str]:
        """Returns a list of all runner emails in the 'Under 20 minutes' category.

        >>> new_race = RaceRegistry()
        >>> new_race.add_runner('toni@mail.utoronto.ca', UNDER20)
        >>> new_race.get_under20()
        ['toni@mail.utoronto.ca']
        """
        return self.registry[UNDER20]

    def get_under30(self) -> List[str]:
        """Returns a list of all runner emails in the 'Under 30 minutes' category.

        >>> new_race = RaceRegistry()
        >>> new_race.add_runner('toni@mail.utoronto.ca', UNDER30)
        >>> new_race.get_under30()
        ['toni@mail.utoronto.ca']
        """
        return self.registry[UNDER30]

    def get_under40(self) -> List[str]:
        """Returns a list of all runner emails in the 'Under 40 minutes' category.

        >>> new_race = RaceRegistry()
        >>> new_race.add_runner('toni@mail.utoronto.ca', UNDER40)
        >>> new_race.get_under40()
        ['toni@mail.utoronto.ca']
        """
        return self.registry[UNDER40]

    def get_above40(self) -> List[str]:
        """Returns a list of all runner emails in the 'Above 40 minutes' category.

        >>> new_race = RaceRegistry()
        >>> new_race.add_runner('toni@mail.utoronto.ca', ABOVE40)
        >>> new_race.get_above40()
        ['toni@mail.utoronto.ca']
        """
        return self.registry[ABOVE40]

    def __str__(self) -> str:
        """Returns a string representation of the runners by email in their groups.
        """
        st = 'The runners are in the following categories:' + '\n'

        for group in self.registry:
            if len(self.registry[group]) != 0:
                st = st + group[0:5].capitalize() + ' ' + group[-2:] + ' minutes:' + '\n'
                for runner in self.registry[group]:
                    st = st + runner + ', '
                st = st[0:-2] + '\n'

        return st

    def __eq__(self, other: Any) -> bool:
        """Returns whether two objects of type RaceRegistry are equal in terms of
        registry content.

        >>> new_race = RaceRegistry()
        >>> new_race.add_runner('toni@mail.utoronto.ca', ABOVE40)
        >>> new_race.add_runner('gerhard@mail.utoronto.ca', UNDER30)
        >>> other_race = RaceRegistry()
        >>> other_race.add_runner('gerhard@mail.utoronto.ca', UNDER30)
        >>> new_race == other_race
        False
        >>> other_race.add_runner('toni@mail.utoronto.ca', ABOVE40)
        >>> new_race == other_race
        True
        """
        return (type(self) == type(other)
                and self.registry == other.registry)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
