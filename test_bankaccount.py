import unittest
from BankAccount import BankAccount


class TestBankAccount(unittest.TestCase):  # test case
    """
    Unit Test for the BankAccount Class
    """

    def setUp(self):  # test fixture
        # print('setup called')
        self.ing = BankAccount('mila', 500)
        self.bnp = BankAccount('alex', 2000)

    def test_deposit(self):
        """ testing the deposit method """
        self.ing.deposit(200)
        self.bnp.deposit(500)

        self.assertEqual(self.ing.balance, 700)
        self.assertEqual(self.bnp.balance, 2500)

    def test_withdraw(self):
        """ testing the withdraw method """
        self.ing.withdraw(400)
        self.bnp.withdraw(1200)

        self.assertEqual(self.ing.balance, 100)
        self.assertEqual(self.bnp.balance, 800)

        self.assertRaises(ValueError, self.ing.withdraw, 500)


if __name__ == '__main__':
    unittest.main()
