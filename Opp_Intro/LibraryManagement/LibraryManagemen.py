class User:
    all_users=[]
    def __init__(self,name,roll,password):
        self.name = name
        self.roll = roll
        self.password=password
        self.borrowed_book=[]
        self.return_book=[]
        

class Library:
    def __init__(self,book_list):
        self.book_list = book_list

    def borrowed_book(self,book_name,user):
        for book in self.book_list:
            if book==book_name:
                if book_name in user.borrowed_book:
                    print("Return the book first")
                    return
                if self.book_list[book] ==0:
                    print("No book is left in library")
                    return
                self.book_list[book] -=1
                user.borrowed_book.append(book)
                print("You have borrowed this book..")
                return
        
        print("Book not avilable!! ): ..")
    def return_book(self,bookName,user):
        for book in self.book_list:
            if book==bookName:
                self.book_list[book]+=1
                user.borrowed_book.remove(bookName)
                user.return_book.append(bookName)
                print("Book returned successfully!!")
                return
            else:
                    print("Thanks but onner boi nibo na")
                    return 
        print("Kar boi ferot dite ashco??")
    
    def availability(self):
        for book in self.book_list:
            if self.book_list[book] > 0:
                print(book,self.book_list[book])
    

    def donate_book(self,book_name,ammount):
        for book in self.book_list:
            if book==book_name:
                self.book_list[book]+=ammount
                print("Thank for donating")
                return
        
        self.book_list[book]=ammount
        print("Thank for donating")
    def all_book(self):
        for book in self.book_list:
            print(book,"=", self.book_list[book],end=' ')
        print("\n")
            





library=Library({"English":2,"Bangla":5,"Math":3})
allluser=[]
currentuser=None

while True:
    if currentuser == None:
        print("No user is logged in!..\n please Login or create Account(L/C)")
        option=input()
        if option == "L":
            roll=int(input("Roll:"))
            password=input("Password: ")
            match=False
            for user in allluser:
                if user.roll==roll and user.password==password:
                    currentuser=user
                    match=True
            if match==False:
                print("No uer found!!")
        else:
            name=input("Name: ")
            roll=int(input("Roll:"))
            password=input("Password: ")
            found=False
            for user in allluser:
                if user.roll==roll:
                    print("Duplicate accounts are not allowed")
                    found=True

            if found:
                print("Duplicate accounts are not allowed")
                continue
            
            

            user=User(name,roll,password)
            currentuser=user
            allluser.append(user)
    else:
        print("Options")
        print("_______")
        print("1.Borrow a book")
        print("2. Return a book")
        print("3. Borrowed books list")
        print("4. Returned books list")
        print("5. Check availability")
        print("6. Donate")
        print("7. Logout")
        x=int(input("Enter option: "))

        if x==1:
            #for book in booklist:
            print("Available book for Borrow")
            library.all_book()
            bookName=input("Book Name:")
            library.borrowed_book(bookName,currentuser)
        elif x==2:
            bookName=input("Book Name:")
            library.return_book(bookName,currentuser)
        elif x==3:
            print("Your borrowd book list are give Below:")
            print(currentuser.borrowed_book)
        elif x==4:
            print("Your return book list are give Below:")

            print(currentuser.return_book)
        elif x==5:
            Library.availability()
        elif x==6:
            bookName = input("Book name: ")
            amount = int(input("Amount: "))
            library.donate(bookName,amount)
        elif x==7:
            currentUser=None 
        print("\n\n")


       
        