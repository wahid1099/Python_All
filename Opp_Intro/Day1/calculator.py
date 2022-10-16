# class Calculator:
#     def add(self, a,b):
#         return a+b
      
#     def subtract(self, a,b):
#         return a-b
#     def multiply(self, a,b):
#         return a*b
#     def divide(self, a,b):
#         return a/b

# my_calcultor=Calculator()
# add=my_calcultor.add(5,5)
# print(add)

# class Sales:
#     def __init__(self, id):
#         self.id = id
#         id = 100

# val = Sales(123)
# print (val.id)

# class People():
#     def __init__(self, name):
#       self.name = name

#     def namePrint(self):
#       print(self.name)



# person1 = People("Emma")
# person2 = People("Watson")
# person2.namePrint()

class Person:
    def __init__(self, id):
        self.id = id

sam = Person(100)
sam.__dict__['age'] = 49

print (sam.age + len(sam.__dict__))