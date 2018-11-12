"""
Test module Stack.
"""
import unittest
from stack import Stack


class EmptyTestCase(unittest.TestCase):
    """Test behaviour of an empty Stac.
    """

    def setUp(self):
        """Set up an empty stack.
        """

        self.stack = Stack()

    def tearDown(self):
        """Clean up.
        """

        self.stack = None

    def testIsEmpty(self):
        """Test is_empty() on empty Stack.
        """
        self.assertTrue(
            self.stack.is_empty(),
            'is_empty returned False on an empty Queue!')


class SingletonTestCase(unittest.TestCase):

    """Check whether adding a single item makes it appear at the back.
    """

    def setUp(self):
        """Set up a Stack with a single element.
        """

        self.stack = Stack()
        self.stack.add('a')

    def tearDown(self):
        """Clean up.
        """

        self.stack = None

    def testIsEmpty(self):
        """Test is_empty() on non-empty Stack.
        """

        self.assertFalse(
            self.stack.is_empty(),
            'is_empty returned True on non-empty Queue!')

    def testRemove(self):
        """Test remove() on a non-empty Stack.
        """

        back = self.stack.remove()
        self.assertEqual(
            back, 'a',
            'The item at the back should have been "a" but was ' +
            back + '.')
        self.assertTrue(
            self.stack.is_empty(),
            'Stack with one element not empty after remove().')


class TypicalTestCase(unittest.TestCase):

    """A comprehensive tester of typical behaviour of Stack.
    """

    def setUp(self):
        """Set up an empty Stack.
        """

        self.stack = Stack()

    def tearDown(self):
        """Clean up.
        """

        self.stack = None

    def testAll(self):
        """Check adding and removing several items.
        """

        for item in range(20):
            self.stack.add(item)
            self.assertFalse(
                self.stack.is_empty(),
                'Stack should not be empty after adding item ' +
                str(item))
        item = 19
        while not self.stack.is_empty():
            back = self.stack.remove()
            self.assertEqual(
                back, item,
                'Wrong item at the back of the Stack. Found ' +
                str(back) + ' but expected ' + str(item))
            item -= 1


if __name__ == '__main__':
    unittest.main(exit=False)
