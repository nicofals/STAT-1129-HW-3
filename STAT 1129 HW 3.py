#!/usr/bin/env python
# coding: utf-8

# In[5]:


marks = {'Andy':88, 'Amy':66, 'James': 90, 'Jules': 55, 'Arthur': 77}
def get_grade(name, marks_dict):
    if name in marks_dict:
        return marks_dict[name]
    else:
        print("Cannot find student with name", name)


# In[6]:


print(get_grade('Andy', marks))
print(get_grade('Jules', marks))  
print(get_grade('Nico', marks)) 


# In[8]:


def squares(num):
    n = 0
    while n < num:
        print(n, n**2)
        n += 1
    else:
        print("greater than", num)
squares(8)


# In[9]:


def number(num):
    total = 0
    n = 1
    while n <= num:
        total += n
        n += 1
    print(total)
number(12)


# In[11]:


def integer(num):
    total = 0
    for n in range(1, num+1):
        total += n
        print(total)
integer(6)


# In[13]:


import statistics
def function(numbers):
    mean = sum(numbers) / len(numbers)
    total = sum(numbers)
    stdev = statistics.stdev(numbers)
    print(mean)
    print(total)
    print(stdev)
numbers = list(range(1, 101))
function(numbers)


# In[14]:


def minimalfunction(v1, v2, v3, v4):
    if v1 <= v2 and v1 <= v3 and v1 <= v4:
        return v1
    elif v2 <= v1 and v2 <= v3 and v2 <= v4:
        return v2
    elif v3 <= v1 and v3 <= v2 and v3 <= v4:
        return v3
    else:
        return v4
result = minimalfunction(6, 12, 1, 16)
print(result)


# In[3]:


def concatenate_strings(str1, str2, str3):
    return str1 + str2 + str3
str1 = "Ciao"
str2 = "bella"
str3 = "!"
concatenated_str = concatenate_strings(str1, str2, str3)
print(concatenated_str)


# In[ ]:




