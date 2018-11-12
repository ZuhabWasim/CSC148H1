"""
An example
"""


class SuperHero(object):
    """ superclass, inherits from default object"""

    def get_name(self):
        """ you want to override this on the child classes"""
        raise NotImplementedError


class SuperMan(SuperHero):
    """subclass, inherits from SuperHero
    """
    def get_name(self):
        """ override"""
        return "Clark Kent"


class SuperManII(SuperHero):
    """ inherits from SuperHero too"""

    def get_name(self):
        """ overrides"""
        return "Clark Kent, Jr."


if __name__ == "__main__":
    sm = SuperMan()
    print(sm.get_name())
    sm2 = SuperManII()
    print(sm2.get_name())
