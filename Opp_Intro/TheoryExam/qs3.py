s = "Programming Hero is the best"
output=" "

brokenwords = s.split(" ")


for word in brokenwords:
    output += word[::-1]+" "


print(output)

