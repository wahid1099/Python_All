# a=int(input('Please enter a: '))
# b=int(input('please enter b: '))

# print(a+b)


# sum=0
# for i in range(0,10):
#     print("Current number",i ,"previes number ",i, "Sum is :", sum)
#     sum+=i


# accept input string from a user
word = input('Enter word ')
print("Original String:", word)

# get the length of a string
size = len(word)

# iterate a each character of a string
# start: 0 to start with first character
# stop: size-1 because index starts with 0
# step: 2 to get the characters present at even index like 0, 2, 4
print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])