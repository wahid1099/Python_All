class Item:
    all=[]
    def __init__(self,itemName,itemPrice)-> None:
        self.__itemName = itemName
        self.__itemPrice = itemPrice
        self.all.append(self)

    def __repr__(self):
        return f"Item {self.itemName},{self.itemPrice}"


item1=Item("Bowl",150)
item2=Item("Plate",200)
item1.__item__discout=100
item1._Item__itemName = "Bowl Broken"
print(item1.__dict__)