"""Notes for week 3
-for assignment 1 there is a demo 1 that is around 5 minutes of assessments
-avoid duplicating documentation
    e.g. superclass and subclass, unless there's no other choice:
    inherited methods, attributes | no need to document again
    extended methods | document that they are extended and how (what's added)
    I overridden methods, attributes | document that they are overridden and how

-pycharm type hinting/contract
    - declaring attributes can have types tooo (x: int)

-list comprehension (copying a new list), aliasing

    instead of

    l = list(range(100))
    new_list = []
    for x in l:
        new_list.append(x * x)

    do this

    new_list = [x * x for x in l] #takes all elements of the previous list
    new_list = [x for x in l if x % 2 ==1] #is a filter, takes only odd numbers

    L = ["one", "two", "three", "four", "five", "six"]
    [s for s in L if s < "one"]
    [s * 3
     for s in L
     if s <= "one"] # written on multiple lines

    you can use this for any iterable type, set, strings, tuples

    [<expression> for <name> in <iterable> if <conditional>]

common Abstract Data Types
    -hide the how (we are doing it)
    -show the what (the ADT does)

    -sequences of items, can be added, removed, accessed by position (lists)
    -specialized list, only have to access recently added item (stacks)
    -collection of items, accessed by associating keys (dictionaries, known as hashes)

Stack class design
    can have
    -things added on top of the stack
    -removed the item from the top of the stack
    -cannot remove anything from an empty stack
    -we need to know if it is empty
    -how big is the stack

    how tho
    -use a python list and use the pop and append method
    -use a python list but add or remove from position 0 (inefficient)
    -use a dictionary with integer keys, keeping track of the lsat index used and which have been removed.

Stack - LIFO, Queue - FIFO

why you need it fam
    -in some situations it is important that openining and closing parentheses, brackets, braces match
    (1 + [7 - {8 / 3}]) good but (1 + 7 [7 - 8{8 / 3]}) is bad

    how can we code this
    -a string with no parentheses is balanced
    -a string that begins with a left parenthesis "(" ends with a right ")" and in between has balanced parenthesis
    is balanced. Same for other brackets
    -the concatenation of two strings with balanced parentheses is also balanced

sack ADT neither FIFO nor LIFO
    -new items added on a random place in the sack
    -order items are removed is unpredictable
    -check if it is empty
    -tell how big it is

generalize stack as Container
    -by generalizing some abstract classes into a super class, we remove the free ability of a programmer to
    have reign over the methods
    -to avoid this we create a super class where everysingle method is pass/raise unimplemented
        -this is so a programmer can create their own Container subclass but the super class provides an interface
        that guides the programmer to code with that specific pattern

Exceptions
    Catches the error and allows continuing of the file, you can write except Exception as e:
    # adding 'as e' tells us what the error was
    the first exception to get raise, all other code cannot be reached
    if that code has a way to handle with the error, it will only handle and treat the first one

    exceptions class
    have an inheritence hierarchy
    has a interface and structure

    catching exceptions have a structure and should generally be from most to least specific
    as more general catches will catch the exceptions that should (more specifically) be caught by the specific clause
    it is designed for

testing
    use doctest but also unit test
    unit test
        -import unit test
        -subclass unittest.Testcase for your tests, and begin each method that carries out a test with the string test
        -compose tests before and during implementation

    test cases
        -you can't think of every case so
        -smallest argument(s): 0, empty list, or string
        -order, permute shuffling
        -boundary case: moving from 0 to 1, empty and non empty
        -typical case

    setUp and tearDown so you have a fresh instance of the class for testing

Sets, has exactly one item in it
    {1, 2, 2, 2, 3, 1, 1, 4} >>> {1, 2, 3, 4}
    order doesn't matter
    {1, 2, 3} == {3, 1, 2, 2} >>> True
    {1, 2, 3} - {1, 2} >>> {3}
    can use mathematical operations such as intersection and union

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
# ##  ###   ####    #####     ######      #######        #######       ######      #####     ####    ###   ##  #
# ##  ###   ####    #####     ######      #######        #######       ######      #####     ####    ###   ##  #
# ##  ###   ####    #####     ######      #######        #######       ######      #####     ####    ###   ##  #
 #  ##   ###    ####     #####      ######       ########       #######      ######     #####    ####   ###  ##
 #  ##   ###    ####     #####      ######       ########       #######      ######     #####    ####   ###  ##
 #  ##   ###    ####     #####      ######       ########       #######      ######     #####    ####   ###  ##
"""
