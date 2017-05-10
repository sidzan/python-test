def outer():
    hi ="hi"
    def inner():
        print (hi)
    return inner

x1 = outer()
print(x1())

