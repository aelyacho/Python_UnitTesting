import unittest
from Person import Person


class TestPerson(unittest.TestCase):
    """
    Unit Test for the Person Class
    """

    def setUp(self):
        """ Instantiating two Person objects"""
        self.p1 = Person('Be', "Code", 4, ['alex', 'mike', 'dave'])
        self.p2 = Person('Su', 'Shi', 22)

    def test_repr(self):
        self.assertEqual(self.p1.__repr__(), 'This is Be Code')
        self.assertEqual(self.p2.__repr__(), 'This is Su Shi')

    def test_add_friend(self):
        self.assertIn('mike', self.p1.friends, msg='mike should be a friend of p1')

        self.p2.add_friend('Billie')
        self.assertIn('Billie', self.p2.friends, msg='Billie should be a friend of p2')

    def test_remove_friend(self):
        self.p1.remove_friend('alex')
        self.assertNotIn('alex', self.p1.friends, msg='alex should not be a friend of p1 anymore')

        self.assertNotIn('Trump', self.p2.friends, msg='Trump is not a friend of p2')


if __name__ == '__main__':
    unittest.main()
