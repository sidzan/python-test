#!/usr/bin/python3
def d (function):
    def wrapper():
        print("i was called")
        return function()
    return wrapper

@d
def display():
    print("display called")

display()
