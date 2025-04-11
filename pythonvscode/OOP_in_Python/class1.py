class Item:
    pay_rate=0.8 #The pay rate after 20% discount
    def __init__(self,name,price : float,quantity):
        #print(f"An instance created : {name}")
        #Run validations to the recieved arguments
        assert price >=0, f"price {price} is not greater than or equal Zero"
        assert quantity >=0, f"price {quantity} is not greater than or equal Zero"
        #Assign to self object
        self.name=name
        self.price=price
        self.quantity=quantity
    def calculate_total_price(self):
        return self.price*self.quantity
    def apply_dicount(self):
        self.price=self.price*self.pay_rate

item1=Item("Phone",100,5)
#item1.name="Phone"
#item1.price=100
#item1.quantity=5
print(item1.name)
print(item1.price)
print(item1.quantity)
print(item1.pay_rate)
#print(item1.calculate_total_price(item1.price,item1.quantity))
print(item1.calculate_total_price())
print('')

item12=Item("Laptop",10000,3)
#item12.name="Laptop"
#item12.price=1000
#item12.quantity=3
print(item12.name)
print(item12.price)
print(item12.quantity)
print(item12.pay_rate)
#print(item12.calculate_total_price(item12.price,item12.quantity))
print(item12.calculate_total_price())
print('')

print(Item.pay_rate)
print('')

#print(Item.__dict__)#All the attributes for class level
print(item1.__dict__)#All the attributes for instance level
print('')
print(item12.__dict__)
print('')

item1.apply_dicount()
print(item1.price)

print('')
item12.pay_rate=0.7
item12.apply_dicount()
print(item12.price)

