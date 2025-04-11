
import csv
class Item:
    pay_rate=0.8 #The pay rate after 20% discount
    all=[]
    def __init__(self,name,price,quantity):
        #print(f"An instance created : {name}")
        #Run validations to the recieved arguments
        assert price >=0, f"price {price} is not greater than or equal Zero"
        assert quantity >=0, f"price {quantity} is not greater than or equal Zero"
        #Assign to self object
        self.name=name
        self.price=price
        self.quantity=quantity
        
        #Actions to execute
        Item.all.append(self)
    def calculate_total_price(self):
        return self.price*self.quantity
    def apply_dicount(self):
        self.price=self.price*self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        with open(r'E:\pythonvscode\OOP_in_Python\items.csv','r') as f:
            reader=csv.DictReader(f)
            items=list(reader)  
        for item in items:
            Item(
                name=item['name'],
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            ) 
    
    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()   
        elif isinstance(num,int):
            return True
        else:
            return False
    def __repr__(self):
        return f"'Item({self.name}',{self.price},{self.quantity})"    
    @property
    def read_only_name(self):
        return "AAAA"







