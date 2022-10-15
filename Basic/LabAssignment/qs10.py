def create_new_string():
    a = ['oh', 'Emelia', 'to']

    s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."
   
    splittedword=s.split(" ")
   

    output="I "
   
    for word in splittedword:
       if word in a:
        indexrep=splittedword.index(word)
        output+=splittedword[indexrep+1]+" "  
       
    file = open("Answer.txt", "w") 
    file.write(output)
    file.close() 
    # return file
 


     
    

create_new_string()