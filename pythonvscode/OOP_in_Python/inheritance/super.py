'''
Super method
super() method is used to access methods of the 
parent class 

'''

class Car:
    color="Black"
    def __init__(self,type):
        self.type=type
        
    @staticmethod
    def start():
        print("Car is started")
        
    @staticmethod
    def stop():
        print("Car is stopped")    

class TyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
        super().start()
        
car1=TyotaCar("prius","Electric")
print(car1.type)  
# car1.start()     