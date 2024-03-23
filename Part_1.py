# Part 1: Bank Account

from random import *


class BankAccount(object):
    def __init__(self, account_holder_name: object, account_number: object, balance: object) -> object:
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self):
        amount = int(input('How much would you like to add to your deposit balance? '))
        self.balance += amount
        print('On your balance:', self.balance)
        return self.balance

    def withdraw(self):
        amount_to_withdraw = int(input('How much would you like to withdraw from your balance? '))
        if amount_to_withdraw > self.balance:
            print('Error')
        else:
            self.balance -= amount_to_withdraw

    def display_balance(self):
        print('On your balance:', self.balance)


name = input('Please enter your full name: ')
number = randint(1000000, 9999999)
print('Welcome to our bank, ' + name + '!')
print('Here is your account number: ' + str(number))
print('The amount of money on your account is: 0')
account = BankAccount(name, number, 0)
account.deposit()
account.withdraw()
account.display_balance()
