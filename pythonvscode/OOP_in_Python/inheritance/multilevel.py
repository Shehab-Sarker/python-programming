class Car:
    color="Black"
    @staticmethod
    def start():
        print("Car is started")
        
    @staticmethod
    def stop():
        print("car is stopped")    

class TyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand
#Multi_levle Inheritance       
class Fortuner(TyotaCar):
    def __init__(self,type):
        self.type=type   
        
car1=Fortuner("Disel")
car1.start() 
print(car1.color)   
car1.stop()      