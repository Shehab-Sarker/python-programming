'''
Important
Abstraction
Hiding the implementation details of a class and only 
showing the essential features to the user.

Encapsulation
Wrapping data and functions into a single unit (object)

'''

class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
        self.speed=False
    def start(self):
        self.clutch=True
        self.acc=True
        print("Car started") 
        
car1=Car() 
car1.start()   

print("")


'''
Let'a Practise
Create Account class with 2
attributes-balance & account no.
Create methods for debit,credit 
& printing the balance.
'''
class Account:
    def __init__(self,bal,acc_no):
        self.balance=bal
        self.account_no=acc_no
    
    def debit(self,amount):
        self.balance-=amount
        print(f"{amount} TK was debited")    
        print("Total balnce =",self.get_balance())
    
    def credit(self,amount):
        self.balance+=amount
        print(f"{amount} TK was credited")    
        print("Total balnce =",self.get_balance())
    
    def get_balance(self):
        return self.balance        
        
acc1=Account(100000,1234)
acc1.debit(5000)
acc1.credit(7000)
      
          
       