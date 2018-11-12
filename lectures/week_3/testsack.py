""" unittests for Sack
"""


import unittest
from sack import Sack


class SackEmptyTestCase(unittest.TestCase):
    """Test behaviour of an empty Sack."""

    def setUp(self):
        """Set up an empty Sack."""
        self.sack = Sack()

    def tearDown(self):
        """Clean up."""
        self.sack = None

    def testIsEmpty(self):
        """Test is_empty() on empty Sack."""
        self.assertTrue(self.sack.is_empty(),
                        'is_empty returned False on empty Sack')

    def testadd(self):
        """Test add to empty Sack."""

        self.sack.add("foo")
        self.assertEqual(self.sack.remove(), "foo",
                         "Wrong item on top of Sack!")


class SackAllTestCase(unittest.TestCase):
    """Comprehensive tests of (non-empty) Sack."""

    def setUp(self):
        """Set up an empty Sack."""
        self.sack = Sack()

    def tearDown(self):
        """Clean up."""
        self.sack = None

    def testAll(self):
        """Test adding and removing multiple elements."""
        number_set = set(range(20))

        for item in number_set:
            self.sack.add(item)
            self.assertTrue(not self.sack.is_empty(),
                            'is_empty returned True on non-empty Sack!')

        while not self.sack.is_empty():
            element = self.sack.remove()
            self.assertTrue(element in number_set,
                            "{} not in {}".format(element, number_set))
            number_set -= {element}


if __name__ == '__main__':
    unittest.main(exit=False)
