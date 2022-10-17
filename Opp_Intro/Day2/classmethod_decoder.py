class Shoppping:
    mall='jamuna Future park'
    hours=[]


    def __init__(self,customer):
        self.customer=customer
        self.items=[]
        self.total=0

    @classmethod
    def opening_hours(cls,day):
        return cls.mall
    
    @staticmethod
    def Multiply(x,y):
        return x*y

    
    def add_to_total(self,ammount):
        self.total+=ammount
    


    def add_to_cart(self,item,price,quantity):
        item_total=price*quantity
        self.add_to_total(item_total)
        self.items.append(item)

    
    def checkout(self):
        pass
