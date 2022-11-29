def mylen(l, n):
    if l == []:
        return n
    else:
        return mylen(l[1:], n+1)
