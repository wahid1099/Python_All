def make_upper(text):
    i=0
    result=""
    while text[i:]:
     ch = ord(text[i])
     if ch >= 97 and ch <= 122:
        result += chr(ch-32)
     else:
        result += chr(ch)
     i += 1
    # print("upper case is",result)
    return result





def make_lower(text):
    i=0
    ch2=""
    while text[i:]:
     ch = ord(text[i])
     if ch >= 64 and ch <= 91:
        ch2 += chr(ch+32)
     else:
        ch2 += chr(ch)
     i += 1
    # print("Lower case is",ch2)
    return ch2


def make_capital(text):
   
    output = text.title() 

    return output
 
    # print("Capitalize",output)



if __name__=="__main__":
    make_upper("hi How ARE you")
    make_lower("hi How ARE you")
    print(make_capital("hi How ARE you")) 





