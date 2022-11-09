def isPlaindromeString(str):
    strlen=int(len(str))

    for i in range(0,int(strlen/2)):
        if str[i] != str[strlen-i-1]:
            return False
    return True


orginalStr=input("Enter a string to check if it si palindrome: ")

checkpalindrm=isPlaindromeString(orginalStr)

if(checkpalindrm):
    print("The string is palindrome!!")
else:
    print("Not palindrome!!")
