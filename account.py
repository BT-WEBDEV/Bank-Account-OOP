#### BANK ACCOUNT APP ####
# Case Use: Quick Practice for OOP - Creating a bank account class
# Bank account has a value stored in balance. You can withdraw & deposit to change your balance. 
# Can be expanded with a GUI.

#base class
class Account: 

    def __init__(self, filepath): 
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount): 
        self.balance=self.balance - amount
        
    def deposit(self, amount): 
        self.balance=self.balance + amount     

    def commit(self): 
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))   

#sub class
class Checking(Account): 
    """ This class generate checking account objects"""
    type="checking"

    def __init__(self, filepath, fee): 
        Account.__init__(self, filepath)
        self.fee=fee
    
    def transfer(self, amount): 
        self.balance=self.balance-amount - self.fee

jacks_checking=Checking("jacks.txt", 1)
jacks_checking.transfer(100)
print(jacks_checking.balance)
jacks_checking.commit()
print(jacks_checking.type)

johns_checking=Checking("johns.txt", 1)
johns_checking.transfer(100)
print(johns_checking.balance)
johns_checking.commit()
print(johns_checking.type)

print(johns_checking.__doc__)

#classes are like blueprints
#objects - they are like variables for classes. Objects store classes
#instance variables - defined within the class method for example withdraw(self,amount)- amount is the instance variable.