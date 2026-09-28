from bank import BankAccount
import pytest


@pytest.fixture
def managed_account():
  print("\n[setup]")
  acc = BankAccount(200)
  yield acc
  print("\n[teardown]")


def test_managed_deposit(managed_account):
  managed_account.deposit(50)
  assert managed_account.balance == 250


def test_managed_withdraw(managed_account):
  managed_account.withdraw(50)
  assert managed_account.balance == 150
