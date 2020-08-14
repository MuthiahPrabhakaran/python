#!/usr/bin/env python
# coding: utf-8

# ### Syntax:
# 
# <pre>
# class x:
#     statements
# 
# class z(<b>x</b>):
#     statements
# 
# class z will inherit all the properties and behaviours from class x
# </pre>

# In[8]:


class A:
    x = 6
    def my_fun(self):
        print("class A")

class B:
    y = 7
    def my_fun(self):
        print("class B")
        return
    
class C:
    z = 8
    def some_fun(self):
        print("class C")
        return
    
class D(A):
    def my_fun1(self):
        print("class D")


# In[9]:


obj = D()
obj.my_fun()
obj.my_fun1()
print(obj.x)


# ### Multiple inheritance is allowed 

# In[16]:


class E(B,C,D):
    def my_fun2():
        print("class E")


# <b>If two class have the same function name, function inside the first class mentioned inside the bracket will get executed</b>

# In[17]:


e = E()


# In[18]:


e.my_fun()

