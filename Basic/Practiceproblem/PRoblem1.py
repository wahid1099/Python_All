phrtron=str(input("Input your string :"))

# length=len(phrtron)

output=''

for i in range(len(phrtron)):
    if(phrtron[i].isupper()):
        output+= phrtron[i].lower()
    else:
        output+= phrtron[i].upper()


print(output)

