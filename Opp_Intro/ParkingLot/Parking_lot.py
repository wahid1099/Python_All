class Car:
    def __init__(self,license,model,color):
        self.license=license
        self.model=model
        self.color=color

    def __repr__(self):
        return f"{self.license},{self.color},{self.model}"


class Garage:
    def __init__(self):
        self.car_adde=[]
        self.spot=10
        self.car_infor={}
        self.bill=0
        self.ticket=[]
    
    def spots_available(self):
        return self.spot
    
    def add_car_to_garage(self,car):
        userdata=car.split(',')
        self.spot_name=['A1','B1','C1','D1','E1','F1','G1']
        if self.spot_name>0:
            pass

