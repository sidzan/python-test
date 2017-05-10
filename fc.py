def square (x):
    return x*x

def cube (x):
    return x*x*x

def map_func(func,arg):
    result = []
    for i in arg:
        result.append(func(i))
    return result

x = map_func(square,[1,2,3,4,5])
y = map_func(cube,x)
print(x)
print(y)
