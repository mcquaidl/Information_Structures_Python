# -*- coding: utf-8 -*-
"""
Larry McQuaid
MET CS 521
10/11/18
Homework 6, Question 12.3
Game:ATM machine
"""

class Account:
    #Store the id, balance, and annual interest rate %
    def __init__(self, identity=0, balance =100.00, interest_rate=0.0):
        self.id = identity
        self.balance = balance
        self.annualInterestRate = interest_rate
    
    #Mutator method for id, balance, & interest rate (redundant??
    def setid(self, identity):
        self.id = identity
    
    def setBalance(self, balance):
        self.balance = balance
        
    def setInterestRate(self, interest_rate):
        self.annualInterestRate = interest_rate    
    
    #Accessor for id, balance, annual & monthly interest rate
    def getid(self):
        return self.id
    
    def getbalance(self):
        return self.balance

    def getMonthlyInterestRate(self):
        return self.annualInterestRate/ 12
    
    #Accessor for monthly interest accrued
    def getMonthlyInterest(self):
        return self.balance * self.getMonthlyInterestRate()
    
    #Function for withdrawing funds if sufficient
    def withdraw(self, withdraw):
            self.balance -= withdraw
    
    #Function for depositing funds
    def deposit(self, deposit):
        self.balance += deposit

def accountInquiry():
    #Create account list
    account_list = []
    
    #Create Accounts 0-9
    for i in range (0,10):
        account = Account(i)
        account_list.append(account)
        
    while True:
        #Asking user to enter account id
        identity = int(input('Enter an account id: '))
        
        #If number entered is greater than 9, ask user to re-enter
        if identity > 9:
            int(input('Please enter a valid ID 0 - 9: '))
        #If number entered is less than 0, ask user to re-enter
        elif identity < 0:
            int(input('Please enter a valid ID 0 - 9: '))
        else:
            True
        #Print out the options for the user
        while True:
            print('\nMain Menu\n1: check balance\n2: withdraw\n3: deposit\
\n4: exit')
            #Ask the user which option they would like to select
            user_selection = int(input('\nEnter a choice: '))
            
            #Ensure that the correct information is reflected for the account
            #selected
            for user_account in account_list:
                if user_account.getid() == identity:
                    accountOpen = user_account
                    break
            
            #Allow the user to check the balance
            if user_selection == 1:
                print('{:.2f}' .format(accountOpen.getbalance()))
            
            #Allow the user to withdraw from their account
            elif user_selection == 2:
                #Ask how much they would like to withdraw
                amount = float(input('Enter an amount to withdraw: '))
                
                #Check to see if the user has sufficient funds to make the 
                #withdrawal
                if amount > accountOpen.getbalance():
                    print('Insufficient funds, your account balance is {}'\
                          .format(accountOpen.getbalance()))
                #Subtract the withdrawal amount from the account and show
                #the balance
                else:
                    accountOpen.withdraw(amount)
                    print('The balance is: {:.2f}' .format(accountOpen.\
                      getbalance()))
            
            #Allow the user to deposit funds into the account
            elif user_selection == 3:
                #Ask the user how much they would like to deposit
                amount = float(input('Enter an amount to deposit: ' ))
                #Add the deposit amount to the account and display the new
                #balance
                accountOpen.deposit(amount)
                print('The balance is: {:.2f}' .format(accountOpen.\
                    getbalance()))
                
            else: 
                break
                
if __name__ == "__main__": 
   accountInquiry() #Call the account inquiry function
        
    
