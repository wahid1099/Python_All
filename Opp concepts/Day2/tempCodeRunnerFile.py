from abc import ABC ,abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    
    def name(self):
        pass