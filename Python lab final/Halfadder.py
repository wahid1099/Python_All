def getHalfadder(A, B):

    sum = A ^ B

    carry = A & B
    return carry, sum


if '__name__' == '__main__':
    while True:
        A = int(input('Enter A value: '))
        B = int(input('Enter B value: '))

        carry, sum = getHalfadder(A, B)
        print('sum:', sum)
        print('carry', carry)
        q = int(input("Do you want to continue \n1.YES\n2.No\n"))
        if q == 2:
            break
