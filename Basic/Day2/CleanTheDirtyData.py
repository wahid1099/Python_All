"""
clean the deta and get a string output 'a,e,i,o,u'
"""

data="aNtEriOur\n\t"

new_data=data.lower()

output_data=''

lenth=len(new_data)
i=0
# print("Lenght is",lenth)
for char in new_data:
   # print(char)
    i+=1
    print(i)
    if(char == 'a') or (char == 'e') or (char == 'i') or (char == 'o') or (char == 'u'):
     output_data+=char
    if(lenth != i):
        output_data+="_"
    # else:
        
        # output_data+=char
        # print("hi")

print(output_data)