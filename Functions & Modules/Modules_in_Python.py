# .py file is a module
#built in module
#math,random,datetime
#How to import a module in a Python
#Syntax: import module_name
#Syntax for importing only few function/variable:from module_name import f1,f2,f3

import math
num=100
output=math.sqrt(num)
print(output)

output=math.pow(num,2)
print(output)

#calculate the area of a circle
radius=5
area=math.pi*radius**2
print(math.pi)
print(f"Area of circle with radius {num} is {area}")

#if not fully importing a module using
from random import randint
value=randint(1,6)
print(value)

#syntax to create an allias for the module that is importes
import datetime as dt
print(dt.time(8,43,51))

