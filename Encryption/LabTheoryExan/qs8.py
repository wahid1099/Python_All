class Book:
    def readingbook():
        with open("File.txt","r") as f:
            isreading=True
            pageskip=False
            # input=None
            for line in f:
                if isreading:
                 browken_words=line.split("--")
                 
                 for i in range(len(browken_words)):
                    index=0
                    i=i+index
                    print("="*80)
                    
                    print("Value of i is ",i)
                    print(browken_words[index]) 
                    userinput=input("[enter - read more, press q to quit]\n")
                    index=int(userinput)
                    print("Value of index is after assigning ",index)
                    i=i+index
                    print("Value of index is after assigning ....",i)
                    print("="*80)

                    
                          

       

Book.readingbook()

