

# while True:

#     num = int(input("Enter a number: "))
#     if num > 0:
#      print("Positive number")
#     elif num == 0:
#      print("Zero")
#     elif num == 'Quit':
#         break
#     else:
#      print("Negative number")




for i in range (1,50,1):
    if i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    elif i%5==0 and i%3==0:
        print("FizzBuzz")
    else:
        print(i)
