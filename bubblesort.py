#!/bin/python3

#def bubbleSort(alist):
    #for passnum in range(len(alist)-1,0,-1):
        #print(passnum)
        #for i in range(passnum):
            #if alist[i]>alist[i+1]:
                #temp = alist[i]
                #alist[i] = alist[i+1]
                #alist[i+1] = temp

#alist = [54,26,93,17,77,31,44,55,20]
#bubbleSort(alist)
#print(alist)


print ("############### binary sort ###########")
alist = [15,20,1,12,35,10]
for num in range(len(alist)-1,0,-1):
    for i in range(num):
        print(i)
        if alist[i]>alist[i+1]:
            temp = alist[i+1]
            alist[i+1] = alist[i]
            alist[i] = temp
print(alist)
print ("#"*20)

data = alist
value = 15 

high = len(data)-1
low = 0 

flag = False
print (low,high)
while (low<=high):
    mid = int((high+low)/2)
    print (data[mid])
    if data[mid] == value:
        print("found")
        flag = True
        break
    if value < data[mid]:
        high = mid-1
    else:
        low = mid+1
if not flag:
    print("not found")



def bubblesort (data,low,high):
    value = 11
    mid = int((high+low)/2)
    if data[mid] == value:
        print("xfound")
        return
    if low==high or high<low:
        raise Exception("cannot find")
    if value < data[mid]:
        bubblesort(data,low,mid-1)
    else:
        bubblesort(data,mid+1,high)

data = alist
high = len(data)-1
low = 0 
bubblesort(data,low,high)







