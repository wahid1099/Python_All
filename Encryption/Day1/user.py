import hashlib
from brta import BRTA
from random import  randint
from Vehicle import Car
from ride_manager import  uber
license_authority=BRTA()
class User:
    def __init__(self,username,email,user_password):
        self.username = username
        self.email=email
        pwd_encypt=hashlib.md5(user_password.encode()).hexdigest()
        
        self.password=user_password
        with open('user.txt','w') as file:
            file.write(f'{email} {pwd_encypt}')
        file.close()

        print(self.username,'User created sucessefully')

    @staticmethod
    def log_in(email, password):
        stored_password =''
        with open('user.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                if email in line:
                    stored_password=line.split(' ')[1]
            file.close()
            hashed_password=hashlib.md5(password.encode()).hexdigest()
            if hashed_password==stored_password:
                print("Valid user")
                return True
            else:
                print("Invalid User")
                return False
            # print("password found",stored_password)


class RIder(User):
    def __init__(self,name,email,password,location,balance) -> None:
     
        self.location = location
        self.balance = balance
        super().__init__(name, email, password)
    
    def setLocation(self,location):
        self.location=location
    
    def get_Location(self):
        return self.location
    

    def requests_trip(self,destination):
        pass
    
    def start_trip(self, fare):
        self.balance -=fare

    


class Driver(User):
    def __init__(self,name,email,password,location,license):
        super().__init__(name,email,password)
        self.location = location
        self.license = license
        self.valid_driver=license_authority.validate_license(email,license)
        self.earings=0

    def take_driving_test(self):
        result=license_authority.take_driving_test(self.email)
        if result==False:
            print("Sorry you falied, try again")
        else:
            self.license=result
            self.valid_driver=True
        
    def register_a_vehicle(self,vehicale_type,license_plate,rate):
        if self.valid_driver is True:
            if vehicale_type=='car':
                new_vehicle=Car(vehicale_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicale_type,new_vehicle)
            elif vehicale_type=='bike':
                new_vehicle=Bike(vehicale_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicale_type,new_vehicle)
            else:
                new_vehicle=CNG(vehicale_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicale_type,new_vehicle)
        else:
            print("You are not a valid driver")
    
    def start_a_trip(self,destination,fare):
        self.earings += fare
        self.location =destination
                
            

      

rider1 = RIder('rider1', 'rider1@gmail.com', 'rider1', randint(0, 30), 5000)
rider2 = RIder('rider2', 'rider2@gmail.com', 'rider2', randint(0, 30), 5000)
rider3 = RIder('rider3', 'rider3@gmail.com', 'rider3', randint(0, 30), 5000)

newuser=User("dummy user","user2@gmail.com","password1234")
# User.log_in("user22@gmail.com","password1234")

driver1 = Driver('driver1', 'driver1@gmail.com', 'driver1', randint(0, 30), 5645)
driver1.take_driving_test()
driver1.register_a_vehicle('car', 1245, 10)


# driver2 = Driver('driver2', 'driver2@gmail.com', 'driver2', randint(0, 30), 5645)
# driver2.take_driving_test()
# driver2.register_a_vehicle('car', 1245, 10)

# driver3 = Driver('driver3', 'driver3@gmail.com', 'driver3', randint(0, 30), 5645)
# driver3.take_driving_test()
# driver3.register_a_vehicle('car', 2145, 10)

# driver4 = Driver('driver4', 'driver4@gmail.com', 'driver4', randint(0, 30), 5645)
# driver4.take_driving_test()
# driver4.register_a_vehicle('car', 3245, 10)


print(uber.get_available_cars())
# uber.find_a_vehicle(rider1, 'car', 90)