import unittest
from Car import Car


class TestCar(unittest.TestCase):
    """
    Unit Testing for Car Class
    """

    def setUp(self):
        self.bmw = Car('BMW', '330', 2015, 'black', 'vrooommmm', 750)
        self.a = Car('a', 'hello', 2020, 'red', 'bzzz', 500)

    def test_drive(self):
        self.assertRaises(ValueError, self.bmw.drive, 800)

    def test_year(self):
        self.assertEqual(self.bmw.year, 2015)
        self.assertEqual(self.a.year, 2020)


if __name__ == '__main__':
    unittest.main()
