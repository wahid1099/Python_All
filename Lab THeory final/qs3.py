
from math import pi

x = 10  # global


def func1():
    x = 20  # local
    print(x)
    print(pi)

    def func2():
        pi = 4  # enclosing scope
        print(pi)
    func2()


func1()
print(x)
