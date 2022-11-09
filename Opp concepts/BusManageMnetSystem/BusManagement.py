class User:
    history =[]
    def __init__(self,username,password):
        self.username = username
        self.password = password


class Bus:
    def __init__(self,coach,driver,arrival,departure,from_dest,to_dest):
        self.coach = coach
        self.driver=driver
        self.arrival = arrival
        self.departure = departure
        self.from_dest = from_dest
        self.to_dest = to_dest
        self.departure=departure

        self.seat=["Empty" for i  in range(20)]

class PhitronCompnay:
    total_bus=5
    total_bus_list=[]


    def install(self):
        bus_no=int(intput("Enter Bus No: "))
        flag=1
        for w in self.total_bus_list:
            if bus_no == w['coach']:
                print("Bus already installed")
                flag=0
                break

        if flag:
            bus_driver=input("Enter Bus driver name : ")
            bus_arrival=input("Enter Bus arrival Time : ")
            bus_departure=input("Enter Bus departure Time : ")
            bus_from = input("Enter Bus Start From : ")
            bus_to = input("Enter Bus To Destination : ")
            self.new_bus = Bus(bus_no, bus_driver, bus_arrival,
                               bus_departure, bus_from, bus_to)
        
        self.total_bus_list.append(vars(self.new_bus))
        print("\n Bus successfully installed...")


class Counter(PhitronCompnay):
    user_list=[]

    def reservation(self):
        bus_no = int(input("Enter Bus No : "))

        for w in self.total_bus_list:
            if bus_no == w['coach']:
                passenger=input("Enter Your Name: ")
                seat_no = int(input("Enter Seat No:"))
                if seat_no>20:
                    print("Seats only 20")
                elif w['seat'][seat_no] != "Empty":
                    print("Sear already booked")
                else:
                    w['seat'][seat_no-1] =passenger
            else:
                print("No bus available")
            
    
    def show(self):
        bus_no=int(input("Enter Bus No : "))
        for w in self.total_bus_list:
            if w['coach']== bus_no:
                print('*'*50)
                print()
                print(f"{'',*10} {'#'*10} Bus Infor {'#'*10}")
                print(f"Bus Number : {bus_no} \t\t Driver : {w['driver']}")
                print(
                    f"Arrival : {w['arrival']} \t\t\tDeparture Time : {w['departure']} \nFrom : \t{w['from_des']} \t\t\tTo : \t{w['to']}")
                print()
                a=1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {w['seat'][a-1]}", end="\t")
                        a+=1
                    for j in range(2):
                        print(f"{a}. {w['seat'][a-1]}", end="\t")
                        a += 1
                    print()

                print("*"*50)

            else:
                print("No bus available")
                break
    def get_user(self):
        return self.user_list
    
    def creat_account(self):
        name = input("Enter your username : ")
        password = input("Enter your password : ")
        self.new_user = User(name, password)
        self.user_list.append(vars(self.new_user))
        print("Account Created Successfully\n")

    def available_bus(self):
        if len(self.total_bus_list == 0):
            print("No bus available..")
        else:
            print('*',*50)

            for bus in self.total_bus_list:
                 print()
                 print(f"{' '*10} {'#'*10} BUS {bus['coach']} INFO {'#'*10}")
                 print(f"Bus number : {bus['coach']} \tDriver : {bus['driver']}")
                 print(
                    f"Arrival : {bus['arrival']} \tDeparture Time : {bus['departure']} \nFrom : \t{bus['from_des']} \t\tTo : \t{bus['to']}")
                 print()
            print('*'*50)

while True:
    company=PhitronCompnay()
    b=Counter()
    print("1. Create an account\n2. login to your account \n3. EXIT\n")
    user_input = int(input("Enter you choice : "))
    if user_input==3:
        break
    elif user_input==1:
        b.creat_account()

    elif user_input==2:
        name=input("Enter your username :")
        password=input("Enter your password :")
        flag=0
        isAdmin=False
        if name=="admin" and password=="123":
            isAdmin=True
        
        if isAdmin == False:
            for user in b.get_user():
                if user['username']== name and user['password']== password:
                    flag=1 
                    break
            if flag:
                while  True:
                    print(f"\n{' '*10}Welcome to BUS TICKET BOOKING SYSTEM")
                    print("1. Available Buses\n2. Show Bus Info\n3. Reservation\n4. EXIT")
                    a = int(input("Enter Your Choice : "))
                    if a == 4:
                        break
                    elif a == 1:
                        b.available_bus()
                    elif a == 2:
                        b.show()
                    elif a == 3:
                        b.reservation()
            else:
                print("No username found")
        else:
            while True:
                print(f"\n {' '*10} HELLO ADMIN Welcome to BUS TICKET BOOKING SYSTEM\n")
                print(
                    "1. Install Bus\n2. Available Buses\n3. Show Bus Info\n4. EXIT")
                a = int(input("Enter Your Choice : "))
                if a == 4:
                    break
                elif a == 1:
                    b.install()
                elif a == 2:
                    b.available_bus()
                elif a == 3:
                    b.show()    

             