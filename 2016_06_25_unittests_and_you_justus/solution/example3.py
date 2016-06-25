"""."""
from unittest import TestCase


class Account:
    """An account stores money."""

    balance = 0

    def deposit(self, amount):
        """Deposit money on this account."""

    def withdraw(self, amount):
        """Withdraw money from this account."""

    def transfer(self, amount, account):
        """Transfer money from one account to another."""


class AccountTestCase(TestCase):
    """."""

    def test_transfer(self):
        pass # TODO
