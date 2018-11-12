"""
Experiment with exceptions changing what is commented out
in the try block
"""


class SpecialException(Exception):
    """class docstring here --- child of Exception"""
    pass


class ExtremeException(SpecialException):
    """ grandchild of Exception"""
    pass


if __name__ == '__main__':
    try:
        # raise SpecialException('I am a SpecialException')
        raise ExtremeException('I am an Exception')

        # raise ExtremeException('I am an ExtremeException')
        # 1/0

    # ... as ??
    # means that ?? is the name of the exception within the
    # except block
    except ExtremeException as ee:
        print(ee)
        print('caught as ExtremeException')
    except SpecialException as se:
        print(se)
        print('caught as SpecialException')
    except Exception as e:
        print(e)
        print("caught as Exception")
