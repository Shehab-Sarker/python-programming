       
from class2 import Item
class Phone(Item):
    def __init__(self,name : str,price:float,quantity=0,broken_phones=0):
        #Call to super function to have access to all attributes / methods
        super().__init__(
           name,price,quantity,
        )
        #print(f"An instance created : {name}")
        #Run validations to the recieved arguments
        # assert price >=0, f"price {price} is not greater than or equal Zero"
        # assert quantity >=0, f"quantity {quantity} is not greater than or equal Zero"
        assert broken_phones >=0, f"broken_phones{broken_phones} is not greater than or equal Zero"
        #Assign to self object
        # self.name=name
        # self.price=price
        # self.quantity=quantity
        self.broken_phones=broken_phones
        

#Inheritance
phone1=Phone("jscPhonev10",500,5,1)
print(phone1.calculate_total_price())
phone2=Phone("jscPhonev20",700,5,1)
print(phone2.calculate_total_price())
# print('')
# print(Item.all)
# print(Phone.all)           