#!/bin/python3
class A(object):
    def foo(cls,x):
        print("x",x)

    @classmethod
    def class_foo(cls,x):
        print("x",x)

A.class_foo(2)
