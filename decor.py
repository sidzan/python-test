#!/bin/python3

print("This is exciting")
def handle_exception(print_msg):
    def inner_handle_exception(function):
        def inner(*args,**kwargs):
            try:
                return function(*args,**kwargs)
            except Exception as e:
                if print_msg:
                    print("The exception is encountered as :",e)
                return 'n/a'
        return inner
    return inner_handle_exception


@handle_exception(True)
def divide(x,y):
    return x/y

@handle_exception(True)
def add (a,b):
    return a+b

print(divide(8,2))
print(add(3,'2'))
