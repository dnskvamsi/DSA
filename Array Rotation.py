#!/usr/bin/env python
# coding: utf-8

# ### Array Rotation

# #####  Let say you have any array of size N. Rotate left to d times

# In[1]:


def leftrotation(arr,d):
    n=len(arr)
    l=d%n
    return arr[l:]+arr[:l]


# In[2]:


print(leftrotation([1,2,3,4,5],2))
print(leftrotation([1,2,3,4,5],7))
print(leftrotation([1,2,3,4,5],1000))
print(leftrotation([1,2,3,4,5],207))
print(leftrotation([1,2,3,4,5],211))


# ### Right Rotation of Array

# In[3]:


def rightrotation(arr,d):
    n=len(arr)
    l=d%n
    return arr[-l:]+arr[0:-l]


# In[4]:


print(rightrotation([1,2,3,4,5],2))
print(rightrotation([1,2,3,4,5],7))
print(rightrotation([1,2,3,4,5],1000))
print(rightrotation([1,2,3,4,5],207))
print(rightrotation([1,2,3,4,5],211))

