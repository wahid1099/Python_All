import csv
from Aircraft import Aircraft

class Airlines:
    def __init__(self)-> None:
        self.air_crafts=None
        self.load_air_crafts_data('./data/aircraft.csv')

    def load_air_crafts_data(self,csv_file):
        air_crafts={}
        with  open(csv_file,'r') as file:
            lines=csv.reader(file)
            next(lines)
            for line in lines:
                #  print(line[3])
                 air_crafts[line[0]]=Aircraft(line[3],line[0],line[1],line[4])
        file.close()
        self.air_crafts = air_crafts
    

    def get_Aircraft(self,code):
        return self.air_crafts[code]


Airlines()

# aircRAT=Aircraft()

# # 
# for Aircrtf in aircRAT.air_crafts:
#     print(Aircrtf)