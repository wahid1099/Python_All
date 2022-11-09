class Star_Cinema():
    _hall_list = []
    def entry_hall(self):
        self._hall_list.append(vars(self))


class Hall(Star_Cinema):
    
    def __init__(self,rows,cols,hall_no):
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.seats = {}
        self.show_list = []
        self.entry_hall()
        
    def entry_show(self):
        id = input('Enter movie id:')
        movie_name = input('Enter movie name:')
        time = input('Enter the movie time:')
        self.show_list.append((id,movie_name,time))
        arr = [[ f"Empty" for i in range(self.__cols)] for j in range(self.__rows)]
        self.seats[id] = arr
    
    def book_seats(self):
        print('*'*50)
        print("Please enter the following information to boook seat:")
        customer_name = input('Enter your name:')
        phone_number = input('Enter your phone number:')
        show_id = input('Enter the show id:')
        flag = True
        for i in self.show_list:
           if i[0] == show_id:
               flag = False
        if flag:
            print('Please! Enter a valid show id.')
        else:
            while True:
                temp = int(input('Do you want to book seat?\n1.Yes\n2.No\n'))
                if temp != 1:
                    break
                row_user = int(input('Enter the row to book seat:'))
                column_user = int(input('Enter the column to book seat:'))
                if row_user-1 < 0 or column_user-1<0 and row_user-1>=self.__rows or column_user-1 >= self.__cols:
                    print('Please! Enter a valid seat no.')
                elif self.seats[show_id][row_user-1][column_user-1]  != "Empty":
                    print('The seat is already booked')
                else:
                    self.seats[show_id][row_user-1][column_user-1] = f'name:{customer_name} , phone:{phone_number}'
                    print('The seat is successfully booked!')
    def view_show_list(self):
        print()
        print('*'*50)
        print()
        print('All shows are:')
        for i in self.show_list:
            print(f'Movie id:{i[0]} {" "*10} Movie Name: {i[1]} {" "*10} Time: {i[2]}')
        print()
        print()   
    def view_available_seats(self,id):
        print()
        print('*'*50)
        flag = True
        cnt = 0
    
        for i in self.show_list:
           if i[0] == id:
               flag = False
        if flag:
            print("Enter a valid id.")
        else:
            print('Available seat are:')
            for i_idx,i in enumerate(self.seats[id]):
                for j_idx,j in enumerate(i):
                    if j == 'Empty':
                        cnt += 1
                        print(f"_{' '*10}",end='')
                    else:
                        print(f"*{' '*10}",end='')
                print()
            print(f'\nTotal available seat:{cnt}')
            
            
class Counter(Hall):
    def __init__(self,other):
        while True:
            temp = int(input('Do you need any query?\n1.Yes\n2.No\n'))
            if temp == 1:
                print("*****Counter****")
                print("1. Running shows")
                print("2. Available seat in a shows")
                print("3. Book a Ticket")
                choice = int(input("Enter your choice:"))
                if choice == 1:
                    other.view_show_list()
                elif choice == 2:
                    id = input('Enter your show id:')
                    other.view_available_seats(id)
                else:
                    other.book_seats()
            else:
                break
        
# all function can be called form counter   

karim = Hall(3,2,50)
karim.entry_show()
karim.entry_show()
karim.entry_show()
counter1 = Counter(karim)