class Star_Cinema:
    hall_list=[]

    def entry_hall(self):
        self.hall_list.append(vars(self))



class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        self.__rows=rows
        self.__cols=cols
        self.__hall_no=hall_no
        self.seats={}
        self.show_list=[]
        self.entry_hall()
    
   


    def entry_show(self):
        id=input("Enter Moview id:")
        movie_name=input("Enter Movie name:")
        time=input("Enter Movie time: ")
        self.show_list.append((id,movie_name,time))
        arr=[["Empty" for i in range(self.__cols)] for j in range(self.__rows)]
        self.seats[id]=arr
    
    def book_seats(self):
        print('-'*80)
        print("Please enter the following information to book  your desired seat:")
        customer_name=input("Enter Name :")
        phone_number=input("Enter Mobile number:")
        show_id=input("Enter Show id: ")
        flag =1
        for i in self.show_list:
           
            if i[0] == show_id:
               flag = 0
        if flag:
             print('Please! Enter a valid show id.')
        else:
          while True:
            userInpt=int(input('Do you want to book seat?\n1.Yes\n2.No\n'))
            if  userInpt == 2: 
                break
            row_user = int(input('Enter the row to book seat (Number input 1 to n):'))
            column_user = int(input('Enter the column to book seat (Number input 1 to n):'))
            if row_user-1<0 or column_user-1<0 and row_user-1 >=self.__rows or column_user-1 >=self.__cols:
                print('Invalid Seat No..')
            elif self.seats[show_id][row_user-1][column_user-1] != 'Empty':
                print("Sorry!.. The seat is already booked..")
            else:
                self.seats[show_id][row_user-1][column_user-1]=f"name:{customer_name},phone:{phone_number}"
                print("Seat booked successfully!!...")

    def view_show_list(self):
        print("Viewing show list...")
        print()
        print("-"*80)
        print("All running shows are :")
        flag=True
        for i in self.show_list:
            print(f"Moview id: {i[0]} ,\t\t  Movie Name: {i[1]} , \t\t Time: {i[2]} ")
            

        print()
        print("-"*80)

    def view_available_seats(self):
            showiduser=input("ENTER SHOW ID: ")
        
            flag=1
            count=0

            for i in self.show_list:
                if i[0] == showiduser:
                    print("-"*80)
                    print(f"MOVIE NAME:{i[1]} \t\t TIME:{i[2]}")
                    flag=0
            if flag:
             print("Enter a valid id...")
            else:
                print("Available seats are:")
                for values in self.seats.values():
                   print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in values]))

                
                
          




wahid=Hall(10,10,50)
# print(vars(wahid))
wahid.entry_show()
wahid.entry_show()
# wahid.entry_show()

while True:
    userinput=int(input('Do you need any query?\n1.Yes\n2.No\n'))
    if userinput == 1:
                print("*****Hall Ticket  Management System****")
                print("1. VIEW ALL SHOWS TODAY ")
                print("2. VIEW AVAILABLE SEATS IN A SHOW")
                print("3. BOOK A TICKET")
                userchoice = int(input("Enter your choice:"))
                if userchoice == 1:
                    wahid.view_show_list()
                elif userchoice == 2:
                    # id=input("Enter your show id:")
                    wahid.view_available_seats()
                else:
                    wahid.book_seats()
    else:
        break


# tesitng
# ds44
# Black Adama
# 5.00 p.m 20Nov 2022
# ds66
# Superman
# 5.00 p.m 20Nov 2022
