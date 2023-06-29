class Item:

    # class attribute
    pay_rate = 0.8
    all = []    
    def __init__(self, name: str, price: float, quantity = 0):
        
          #running validations
        assert price>=0, f"price {price} is not greater than or equal to zero"
        assert quantity>=0, f"price {quantity} is not greater than or equal to zero"

  
        #assign self to object
        self.name = name
        self.price = price
        self.quantity = quantity

        # actions to execute
        Item.all.append(self)

    
    def calculate_total_price(self):
        return self.price * self.quantity

        
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # magic method
    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})" 
    

item1 = Item("phone", 100, 1)
item2 = Item("laptop", 1000, 3)
item3 = Item("cable", 10, 5)
item4 = Item("house", 50, 5)
item5 = Item("keyboard", 75, 5)

print(Item.all)