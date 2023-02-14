class Person:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        
class Customer(Person):
    def __init__(self,first_name,last_name,account_number,balance=0):
        super().__init__(first_name,last_name)
        self.account_number=account_number
        self.balance=balance
    
    def __str__(self):
        return f"the person {self.first_name} {self.last_name} has {self.account_number} and {self.balance} of balance"   
        
    def deposite(self,cash): 
        self.balance+=cash
        return self.balance
        
    def withdraw(self,cash):
        if self.balance>=cash:
            self.balance-=cash
            return self.balance
        else:
            print("insufficient balance")
        
def create_client():
       first=input("digit the first name: ")
       last=input("digit the last name: ")
       account_number=input("digit the account number: ")
       client=Customer(first,last,account_number)
       return client

def start():
    mode=False
    cliente=create_client()
    while not mode:
        print("do you want make a deposit or withdraw? ")   
        answer=input()
        if answer=="deposit":
            print("how much cash do you want")
            cash = int(input())
            cliente.deposite(cash)
            print(str(cliente))
        elif answer=="withdraw":
            print("how much cash do you want")
            cash = int(input())
            cliente.withdraw(cash) 
            print(str(cliente))   
        elif answer=='exit':
            mode=True
        else:    
            print("invalid answer")    
            
start()            
        
            
