def exp(a,n):
    expo=pow(a,n)
    return expo

# x, y = [int(x) for x in input().split()]  
x, y = input().split()
x, y = [int(x), int(y)]
ans=exp(x, y)
print("result is:",ans)
