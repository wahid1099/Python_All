class Laptop:
    def __init__(self,brand,age):
        self.brand=brand
        self.age=age

    def increse_age(self,age=1):
        self.last_age=self.age
        self.age=self.age+age

    def repair(self, life_increase = -5):
        self.increse_age(life_increase)

myLaptop=Laptop('Hp',3)
myLaptop.increse_age()
print(myLaptop.age)

myLaptop.increse_age()

print(myLaptop.age)
myLaptop.repair()
print(myLaptop.age)
print(myLaptop.__dict__)