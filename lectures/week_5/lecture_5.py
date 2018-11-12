"""Lecture 5 Notes
Python pep tide
- don't re-invent the wheel e.g. sum, set
- use comprehensions when you mean to produce a new list
    - like list comprehensions but for sets, dictionaries, etc
    - generator comprehensions
    - used when you're creating a new object from an old one.
- exists: any and for all: all (any and all are python keywords)
- ternary operators when we want to express a value differently based on a condition
    - expr1 if ___ else expr2

- Uses for list comprehensions
    - Proving statements
        e.g. create a list of the cubes from 1 to 11.
        [x ** 3 for x in range(1,11)]

        is the sum of any cube a square?
        sum([x**3 for x in range(1,11)]) >>> 3025
        3025**0.5 >>> 55.0

        [sum([x**3 for x in range(1,n)]) for n in range(11)]

    - brevity and clarity, euclidean distance
        def euclidean_distance(list_: list) -> float:
            return sum([x**2 for x in list_]) ** 0.5
        euclidean_distance([3, 4, 12]) >>> 13.0

    - with open("/usr/share/dict/words", "r") as words_file:
        word_list = words_file.read().split("\n")

    - average string lengths
        sum([len(x) for x in word_list]) / len(word_list) >>> 8.46

    - quantifiers
        - any (returns True if you have a list of iterables of which any can be evaluated to true or false
            - any([0, 0.2, [], None]) >>> False
            - any([0, 0.2, [], True, None]) >>> True
            - any([0, 0.2, [], 7, None]) >>> True

        - all([]) is True --> returns True if none of the values in the iteratble is false

        - all([len(s) > 0 for s in word_list]) >>> False so there is one empty list in the file
            [s for s in word_list if len(s) == 0]

        - any[('yxy; in s for s in word_list)] looks through every element to see if atleast one works
        but any(('yxy; in s for s in word_list)) ends search early (once the condition is met) for efficiency

- sets
    - a list with no duplicates
    - note you can sort a list by writing sorted(list)

- thoughtful wishing
have code that calls functions that don't even exist yet to make sure you code the whole correctly



"""
