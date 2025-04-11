
class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name, price, quantity):
        # print(f"An instance created : {name}")
        # Run validations to the recieved arguments
        assert price >= 0, f"price {price} is not greater than or equal Zero"
        assert quantity >= 0, f"price {quantity} is not greater than or equal Zero"
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_dicount(self):
        self.price = self.price * self.pay_rate

    # def instantiate_from_csv(cls):
    #     with open('items.csv', 'r') as f:
    #         reader = csv.reader(f)
    #         items = list(reader)
    #     for item in items:
    #         print(item)

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

# Item.instantiate_from_csv()

# print(Item.all)
# print(item1.__dict__)
# print(item2.__dict__)
# print(item3.__dict__)
# print(item4.__dict__)
# print(item5.__dict__)



