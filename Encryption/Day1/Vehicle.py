from abc import ABC,abstractmethod

class Vehicle(ABC):
    speed={
        'car':30,
        'bike':50,
        'cng':15
    }

    def __init__(self,vehicle_type,licencse_plate,rate,driver)-> None:
        self.vehicle_type = vehicle_type
        self.rate=rate
        self.driver=driver
        self.status='avaible'
        self.licencse_plate=licencse_plate
        self.speed=self.speed[vehicle_type]
    @abstractmethod
    def start_drive(self):
        pass
    @abstractmethod
    def trip_finished(self):
        pass

class Car(Vehicle):
    def __init__(self,vehicle_type,licencse_plate,rate,driver)-> None:
        super().__init__(vehicle_type,licencse_plate,rate,driver)

        def start_drive(self):
            self.status='unavailable'
            print(self.vehicle_type,self.licencse_plate,
            'started')
        def trip_finished(self):
            self.status='available'
            print(self.vehicle_type,self.licencse_plate,
            'Trip completed!!')

class Bike(Vehicle):
     def __init__(self,vehicle_type,licencse_plate,rate,driver)-> None:
        super().__init__(vehicle_type,licencse_plate,rate,driver)
        def start_drive(self):
            self.status='unavailable'
            print(self.vehicle_type,self.licencse_plate,
            'started')
        def trip_finished(self):
            self.status='available'
            print(self.vehicle_type,self.licencse_plate,
            'Trip completed!!')


class CNG(Vehicle):
    def __init__(self,vehicle_type,licencse_plate,rate,driver)-> None:
        super().__init__(vehicle_type,licencse_plate,rate,driver)
        def start_drive(self):
            self.status='unavailable'
            print(self.vehicle_type,self.licencse_plate,
            'started')
        def trip_finished(self):
            self.status='available'
            print(self.vehicle_type,self.licencse_plate,
            'Trip completed!!')
    
