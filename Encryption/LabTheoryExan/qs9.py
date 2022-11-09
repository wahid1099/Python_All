class Book:
    def readingbook():
        with open("File.txt","r") as f:
            file_data = f.read()
            data_into_list = file_data.split('--')
            # print(data_into_list[1])
            pageskip=True
            isreading=True
            index=0
            for i in range(len(data_into_list)):
                if isreading:
                    # if pageskip:
                    #  index+=i
                
                    print(data_into_list[index])
                    
                    userinput=input("[enter - read more, press q to quit]\n")
                    if userinput == 'q':
                        isreading=False
                        break
                    elif userinput.isdigit():
                      
                        
                      pagenumer=int(userinput)
                      
                      index+=pagenumer
              
                      pageskip=False
                    elif userinput == '-':
                         index+=1
                         pageskip=True
                    elif userinput[0] == '-' and userinput[1].isdigit() :
                        backpage=int(userinput[1])
                        index-=backpage
                        pageskip=False
                    else:
                        pass
                

            f.close()
           

       

Book.readingbook()

