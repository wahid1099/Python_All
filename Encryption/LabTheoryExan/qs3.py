def nearly_equal(str1,str2):
    count=0
    i=0
    j=0
    while(i<len(str1) and j<len(str2)):
        if(str1[i]!=str2[j]):
            count=count+1
            if(len(str1)>len(str2)):
                i=i+1
            elif(len(str1)==len(str2)):
                pass
            else:
                i=i-1
        if(count>1):
            return False
        i=i+1
        j=j+1
    if(count<2):
        return True

checknearlyequal = nearly_equal('perl', 'pearl') 

if checknearlyequal:
    print("Yes")
else:
    print("No")
        


