
####--------simple function--------####

def function_name(a,b,c):
    print(a,b,c)
function_name("altaf","zohaib","muzammil")

####--------args function-----------####

def function_name(l):
    print(l)
function_name("altaf","zohaib","muzammil")
function_name(list)

###----------args function---------###

def function_name(**args):
    for item in args:
       print(item)
function_name("altaf","zohaib","muzammil")

###-------------list args function-----###

def function_name(s,*args):
    print(s)
    for item in args:
        print(item)
list=["altaf","zohaib","muzammil"]
str = "i am good boy"
function_name(str,*list)

###---------kwargs function-------###

def function_name(**kwargs):
   for key, Value in kwargs.items():
        print(key,Value)
function_name(f1="altaf",f2="zohaib",f3="muzammil")      

###---------kwargs function-------###

def function_name(**kwargs):
    for key, Value in kwargs.items():
        print(key,Value)
dic ={"f1":"altaf","f2":"zohaib","f3":"muzammil"} 
function_name(**dic)


###--------re match function--------###

import re

s = 'Today is wednesday and tomorrow is Thusday'
p = re.match('Today.*',s)
if p:
    print('found match')
else:
    print('no match')