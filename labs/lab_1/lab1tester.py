"""
Module that tests the lab1.py module for correctness.
"""

if __name__ == '__main__':
    #from labs import lab_1
    import lab1

    UNDER20 = 'under20'
    UNDER30 = 'under30'
    UNDER40 = 'under40'
    ABOVE40 = 'above40'

    race_registry = lab1.RaceRegistry()

    race_registry.add_runner('gerhard@mail.utoronto.ca', UNDER40)
    race_registry.add_runner('tom@mail.utoronto.ca', UNDER30)
    race_registry.add_runner('toni@mail.utoronto.ca', UNDER20)
    race_registry.add_runner('margot@mail.utoronto.ca', UNDER30)
    race_registry.add_runner('gerhard@mail.utoronto.ca', UNDER30)

    print(race_registry)
