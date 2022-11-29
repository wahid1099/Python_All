def mylen(l, n):
    if l == []:
        return n
    else:
        return mylen(l[1:], n+1)


def mylen(l, n):

    while l != []:
        l = l[1:]
        n = n+1

    return n


lenth = mylen([1, 2, 3, 4, 1, 1, 5, 6, 5], 0)

print("lenth is", lenth)
