# -*- coding: utf-8 -*-
"""
Used to find the flow of code
pdb - python debug

We can decode with pdb module also. We can debug in the editor
"""

import pdb


"""
for i in range(10):
    x = i*4
    print(i,x)
    # Programatically putting break point
    pdb.set_trace()
"""

def transform(x,y):
    x = x**2
    y = y*2
    z = x+y
    return z

x = 1000
y = 20
pdb.set_trace()
print(transform(x,y))

    
"""
n - go to next line
c - one cycle gets completely executed
l - shows previous and next 3 lines from current line
s - steps into a function
q - quitting debug mode
b - list of break points(it won't show a programatic break point)
b[int] - set a break point at a particular line number
Example: b 21
         b transform

b[function] - set a bp for a function
cl - clear the break point



type the variable name to find out the value of the same.
If the variable name is a keyword(like n), then type p(variable_name) to find out the value
"""