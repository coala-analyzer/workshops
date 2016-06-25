"""."""
from unittest import TestCase


class Account:
    """An account stores money."""

    def __init__(self):
        self.transactions = []

    def deposit(self, amount):
        """Deposit money on this account."""
        self.transactions.append(amount)

    def withdraw(self, amount):
        """Withdraw money from this account."""
        self.transactions.append(-amount)

    @property
    def balance(self):
        """Report current balance."""
        return sum(self.transactions)


class AccountTestCase(TestCase):
    """."""

    def setUp(self):
        self.account = Account()

    def test_no_transaction(self):
        self.assertEqual(self.account.balance, 0)

    def test_deposit(self):
        self.account.deposit(9001)
        self.assertEqual(self.account.balance, 9001)

    def test_withdraw(self):
        self.account.withdraw(9001)
        self.assertEqual(self.account.balance, -9001)
