#!/bin/python3h
def add (a,b):
    return a+b

def subtract (a,b):
    return a-b

def sort_data(data):
    print (data," ## data")
    return a = data.sort()

import unittest
class OutcomesTest(unittest.TestCase):
    data = [9,7,2,4,8]

    def test_add(self):
        self.assertEquals(add(2,3),2+3)

    def test_subtract(self):
        self.assertEquals(subtract(3,2),3-2)

    def test_sort(self):
        self.assertEquals(sort_data(self.data),[2,4,7,8,9])



unittest.main()

print ("Called")
