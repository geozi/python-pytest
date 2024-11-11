from random import randint

class BankAccount:
    
    """
    The BankAccount class is the abstract representation of a simple bank account with limited functionality.

    """    
    
    account_id = ''.join([str(randint(0, 9)) for _ in range(12)])
    
    def __init__(self, balance):
        self.__balance = balance
        
    # Getters 
    
    @property
    def balance(self):
        return self.__balance
        
    # Operations
    
    def deposit(self, amount):
        isSuccessful = False
        if amount >= 0:
            self.__balance += amount
            isSuccessful = True 
        return isSuccessful
        
    def withdraw(self, amount):
        isSuccessful = False;
        if self.__balance >= amount:
            self.__balance -= amount
            isSuccessful = True
        
        return isSuccessful
    
    