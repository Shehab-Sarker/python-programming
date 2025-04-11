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

# item1=Item("Phone",100,5)
# item2=Item("Laptop",1000,3)
# item3=Item("cable",10,5)
# item4=Item("Mouse",50,5)
# item5=Item("keyboard",75,5)

# for i in Item.all:
#     print("Name:",i.name)
#     print("Price:",i.price)
#     print("Quantity:",i.quantity)
#     print('')

#Item.instantiate_from_csv()

#print(Item.all)    
# print(item1.__dict__)    
# print(item2.__dict__)    
# print(item3.__dict__)    
# print(item4.__dict__)    
# print(item5.__dict__)   

#print(Item.is_integer(7.0)) 

# class Phone(Item):
#     all=[]
#     def __init__(self,name : str,price:float,quantity=0,broken_phones=0):
#         #Call to super function to have access to all attributes / methods
#         super().__init__(
#             name=name,
#             price=price,
#             quantity=quantity,
#         )
#         #print(f"An instance created : {name}")
#         #Run validations to the recieved arguments
#         # assert price >=0, f"price {price} is not greater than or equal Zero"
#         # assert quantity >=0, f"quantity {quantity} is not greater than or equal Zero"
#         assert broken_phones >=0, f"broken_phones{broken_phones} is not greater than or equal Zero"
#         #Assign to self object
#         # self.name=name
#         # self.price=price
#         # self.quantity=quantity
#         self.broken_phones=broken_phones
        
#         #Actions to execute
#         Phone.all.append(self)
# #Inheritance
# phone1=Phone("jscPhonev10",500,5,1)
# print(phone1.calculate_total_price())
# phone2=Phone("jscPhonev20",700,5,1)
# print(phone2.calculate_total_price())
# print('')
# print(Item.all)
# print(Phone.all)