n = int(input())


for j in range(2, n+2):
    for k in range(2, n+2):
        # print(k, end="")
        if (k < n+1):
            if (j == k):
                print("1", end="")
                print(k, end="")
            else:
                print(k, end="")
    if j == n+1:

        print("1", end="")

    print("")
