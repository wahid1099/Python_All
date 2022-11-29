# def max(l, n):
#     if l == []:
#         return n
#     elif l[0] > n:
#         return max(l[1:], l[0])
#     else:
#         return max(l[1:], n)


# arr = [1, 4, 3, 5, 4, 8, 6]
# maximum = max(arr, 9)
# print("maximum is ", maximum)


def max(l, n):
    max = l[0]
    for i in range(len(l)):
        if l[i] > n and l[i] > max:
            max = l[i]
        elif n > l[i]:
            max = n

    return max


# arr = [1, 4, 3, 5, 4, 8, 6]
# maximum = max(arr, 4)
# print("maximum is ", maximum)
