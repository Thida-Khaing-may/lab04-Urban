#test_withdraw.py
from bank import BankAccount
import pytest


@pytest.fixture
def account():
  return BankAccount(100)


def test_withdraw_reduces_balance(account):
  account.withdraw(40)
  assert account.balance == 60


def test_withdraw_overdraft_raises_error(account):
  with pytest.raises(ValueError, match="Insufficient funds"):
    account.withdraw(200)