#!/bin/python3

import time
from time import sleep

class Person (object):
    id = 0
    name = None
    fields = None

    def __init__(self):
        ctime = time.strftime("%Y-%m-%d %H:%M:%S")
        self.fields.update({"create_time":ctime,
                            "write_time" :ctime})

    def check_keys (self,vals):
        for k in vals:
            if not k in self.fields.keys():
                raise Exception("Key %s doesnot exists"%k)

    def update(self,*args,**kwargs):
        vals = kwargs['vals']
        self.check_keys(vals)
        self.fields.update(vals)
        ctime = time.strftime("%Y-%m-%d %H:%M:%S")
        self.fields.update({"write_time":ctime})

    def write(self,*args,**kwargs):
        vals = kwargs['vals']
        self.check_keys(vals)
        self.fields.update(vals)

    def detail (self):
        print ("Model Name is ",self.name)
        for k,v in self.fields.items():
            print("key:",k," value:",v)
        print ("#"*50)

class Contact (Person):
    
    id = 0
    def __init__(self):
        self.name="contact"
        self.fields = {
            'id':None,
            'name':None,
            'age':None
        }
        Contact.id+=1
        super(Contact,self).__init__()

    def get_id(self):
        return self.id
        

ca = Contact()
ca.write(vals={'name':'sijan','age':31,'id':ca.get_id()})
sleep(1)
ca.update(vals={'name':'sijan Shs'})
ca.detail()

cb = Contact()
cb.detail()
cb.write(vals={'name':'Aurelia','age':32,'id':cb.get_id()})

cc = Contact()
cc.detail()
cc.update(vals={'name':'React','age':33,'id':cc.get_id()})

print ("calling contact 1")
ca.detail()
print ("calling contact 2")
cb.detail()
print ("calling contact 31")
cc.detail()
