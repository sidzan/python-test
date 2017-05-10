#!/bin/python3
total = 8

a = [1,2,3,4,5,6,7,8,9]

low = 0
high = len(a)-1

while(low<high):
    s = a[low]+a[high]
    if s == total:
        print("found",a[low],a[high])
    if s<total:
        low+=1
    else:
        high-=1



