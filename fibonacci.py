#!/bin/python3

def fib(num):
    a,b = 0,1
    while (a<num):
        print (a)
        a , b = b,a+b
fib(100)
x = [x*x for x in range(1,6,2)]
print(x)
