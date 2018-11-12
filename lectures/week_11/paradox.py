"""experiment with birthdays
"""""


from random import randint


def birthday_experiment(n):
    """
    Report n instances of the birthday paradox.

    @param int n: number of repeats
    @rtype: None
    """
    for i in range(n):
        seen = set()
        collision = False
        birthdays = 0
        days_in_year = 366
        while not collision:
            birthdays += 1
            birthdate = randint(1, days_in_year)
            if birthdate in seen:
                collision = True
                print("Collision at birthday {}!".format(birthdays))
                print("Percent: {}".format(100 * birthdays / days_in_year))
            else:
                seen.add(birthdate)

if __name__ == "__main__":
    birthday_experiment(5)