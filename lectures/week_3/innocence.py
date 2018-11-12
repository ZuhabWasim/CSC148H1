"""
get exposed to various mischief...
"""
from mystery import wtf


if __name__ == "__main__":
    try:
        wtf()
    except IndexError as e: # Catches the error and allows continuing of the file, you can write except Exception ase:
        print("oooops!") # adding 'as e' tells us what the error was.
        print(e)
    except ZeroDivisionError as e:
        print("double ooops!")
        print(e)
    except Exception as e:
        print("general ooops!")
        print(e)
    print("we got through it!")
