def do_something():
    print("Inside the function do something...")
    def inner_function():
        print("Inside the function inner_function")
    inner_function()


# do_something()


def first_function():
    print("Inside the  first_function")
    def second_function():
        print("Inside the  second_function")
    return second_function()


first_function()()