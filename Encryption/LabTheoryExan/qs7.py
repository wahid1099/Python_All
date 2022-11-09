class Book:
    def readingbook():
        with open("File.txt","r") as f:
            isreading=True
            for line in f:
                if isreading:
                 browken_words=line.split("--")
                 for word in browken_words:
                    print(word) 
                    userinput=input("[enter - read more, press q to quit]\n")
                    if userinput == 'q':
                        isreading=False
                        break
        
       

Book.readingbook()

