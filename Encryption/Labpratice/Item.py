import json
class Item:
    all=[]
    def __init__(self,name,price):
        self.name=name
        self.price=price


    def initialize():
        with open("./extract.txt", "r") as f:
            data=f.read()
            js=json.loads(data)
        for item in js:
            print(item)
        for item in js:
            Item(
                name=item["name"],
                price=item.get("price")
            )
    def __repr__(self) -> str:
        return f"Item({self.name},{self.price})"

Item.initialize()
print(Item.all)