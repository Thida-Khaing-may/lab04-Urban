# test_shared.py
def test_shared_fixture_initial_balance(funded_account):
    assert funded_account.balance == 1000

def test_shared_fixture_withdraw(funded_account):
    funded_account.withdraw(300)
    assert funded_account.balance == 700