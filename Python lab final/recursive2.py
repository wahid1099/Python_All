def max(l, n):
    if l == []:
        return n
    elif l[0] > n:
        return max(l[1:], l[0])
    else:
        return max(l[1:], n)


arr = [1, 4, 3, 5, 4, 8, 6]
maximum = max(arr, 4)
print("maximum is ", maximum)
