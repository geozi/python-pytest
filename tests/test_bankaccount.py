from src.bank_account import BankAccount 
import pytest

# Positive scenarios 

def test_account_balance_without_ops():
    account = BankAccount(0)
    
    assert account.balance == 0

def test_account_balance_after_deposit():
    account = BankAccount(0)
    op_result = account.deposit(1000)
    
    assert op_result
    assert account.balance == 1000

def test_account_balance_after_withdrawal():
    account = BankAccount(200)
    op_result = account.withdraw(100)
    
    assert op_result
    assert account.balance == 100

def test_account_balance_with_mixed_ops():
    account = BankAccount(200)
    op_result = account.deposit(1000)
    op_result = account.withdraw(500)
    op_result = account.deposit(200)
    op_result = account.withdraw(600)
    
    assert op_result
    assert account.balance == 300

# Negative scenarios 

def test_account_balance_with_deposit_on_none():
    account = BankAccount(None)
    with pytest.raises(TypeError):
        op_result = account.deposit(1)

def test_account_balance_with_withdrawal_on_none():
    account = BankAccount(None)
    with pytest.raises(TypeError):
        op_result = account.withdraw(1)

def test_account_balance_with_deposit_on_string():
    account = BankAccount(" ")
    with pytest.raises(TypeError):
        op_result = account.deposit(1)

def test_account_balance_with_withdrawal_on_string():
    account = BankAccount(" ")
    with pytest.raises(TypeError):
        op_result = account.withdraw(1)

def test_account_balance_with_negative_deposit():
    account = BankAccount(0)
    op_result = account.deposit(-100)
    assert not op_result

def test_account_balance_with_overdraw():
    account = BankAccount(1000)
    op_result = account.withdraw(1200)
    assert not op_result