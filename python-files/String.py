#!/usr/bin/env python
# coding: utf-8

# In[1]:


fruit = "banana"
print(fruit[1])


# In[2]:


print(fruit[10])


# In[4]:


print(len(fruit))


# In[5]:


index = 0
while(index<len(fruit)):
    letter = fruit[index]
    print(index, letter)
    index +=1


# In[6]:


for c in fruit:
    print(c)


# In[4]:


word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count += 1
print('count of a\'s', str(count))        


# ## Slicing String

# In[8]:


s = 'Monty Python'
print(s[0:6])
print(s[:3])
print(s[6:])
print(s[:-4])


# ## Concatenation

# In[9]:


a = 'Hello'
b = a + ' ' + 'World'
print(b)


# ## in in String

# In[11]:


fruit = 'banana'
print('b' in fruit)
print('nana' in fruit)


# ## String comparison
# It will compare as in Dictionary order(lexicograph ordering)

# In[19]:


country = 'India'
print(country < 'Australia')
print(country > 'Australia')
print(country < 'india')
print([2,2] > [1,10]) #It will compare from left to right
print("t5" > "5t") #Alphabets are bigger than the digits


# In[27]:


dir(country)


# In[28]:


get_ipython().run_line_magic('pinfo', 'country.lower')


# In[30]:


"How are you?".upper().split()


# In[32]:


"       How are you?       ".strip()


# ## Search and Replace

# In[33]:


print("Hello John".replace("John", "Bob"))


# In[ ]:




