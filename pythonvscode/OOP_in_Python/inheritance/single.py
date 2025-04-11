'''
Inheritance
When One class(child/derived) derives the 
properties & methods of another class(parent/base).

class Car:
   ......

class ToyotaCar(Car):
    .......
'''   

class Car:
    color="Black"
    @staticmethod
    def start():
        print("Car is started")
        
    @staticmethod
    def stop():
        print("car is stopped")    
#Single Inheritance
class TyotaCar(Car):
    def __init__(self,name):
        self.name=name
        
car1=TyotaCar("fortuner")
car2=TyotaCar("prius")

car1.start() 
print(car2.color)       



