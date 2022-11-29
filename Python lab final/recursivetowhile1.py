# def sum_odd(n, total):
#     if n == 1:
#         return total
#     elif n % 2 == 0:
#         return sum_odd(n-1, total)
#     else:
#         return sum_odd(n-2, total+2)


# ans = sum_odd(10, 0)

# print("ans", ans)


def sum_odd(n, total):

    while n != 1:
        if n % 2 == 0:
            n = n-1
        else:
            n = n-2
            total = total+2
    return total


# ans = sum_odd(10, 0)
# print("sum is ", ans)
