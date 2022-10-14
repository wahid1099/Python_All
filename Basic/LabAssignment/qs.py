def clean_string(text):
    output=""
    for i in text:
        if i>='A' and i<='Z':
            output += i
        elif i>='a' and i<='z':
            output += i
   
    return output
    
    

s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"
output = clean_string(s)
print(output)

