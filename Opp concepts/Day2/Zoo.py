from abc import ABC ,abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    
    def name(self):
        pass

    def move(self):
        pass


class Monkey(Animal):
    def sing(self):
        print("Inside the Monkey")
    def eat(self):
        pass
    

lykey=Monkey()
print(Monkey)