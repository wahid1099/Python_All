class Person:
    def __init__(self,name,phone,age)-> None:
        assert age>13,f"Only greater than 13 allowed"
        assert len(phone)==11,f"Invalid phone number:"
        self.name = name
        self.phone = phone
        self.age = age
        
        def __repr__(self)->str:
            return f"{self.name} {self.phone} {self.age}"
    
user=Person("wahid","01879439753",14)
print(user)
