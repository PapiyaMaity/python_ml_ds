#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[4]:


arr=np.arange(0,11)
arr


# In[14]:


arr=np.linspace(0,50,11)
arr


# In[15]:


arr[5]


# In[16]:


arr[:5]


# In[17]:


arr[5:]


# In[19]:


bool_arr=arr>25
bool_arr


# In[20]:


arr[[5,6]]


# In[24]:


arr_c=arr[bool_arr]
arr_c


# In[23]:


arr_copy=arr_c.copy()
arr_copy


# In[25]:


dice_rolls = np.array([3, 1, 5, 2, 5, 1, 1, 5, 1, 4, 2, 1, 4, 5, 3, 4, 5, 2, 4, 2, 6, 6, 3, 6, 2, 3, 5, 6, 5])
dice_rolls


# In[27]:


bool_arr=dice_rolls>2
bool_arr


# In[28]:


arr=dice_rolls[bool_arr]
arr


# In[33]:


len(arr)


# In[1]:


import numpy as np


# In[2]:


arr=np.arange(0,11)


# In[3]:


arr


# In[4]:


arr.max()


# In[6]:


arr.min()


# In[7]:


arr.sum()


# In[8]:


arr.shape


# In[14]:


arr - arr[10]


# In[19]:


len(arr)


# In[4]:


arr=np.linspace(0,9,3)


# In[5]:


arr


# In[6]:


arr.reshape(3,1)


# In[7]:


np.ones(10)*5


# In[10]:


arr=np.arange(0,9)


# In[11]:


arr


# In[12]:


arr.reshape(3,3)


# In[14]:


arr=np.eye(3)
arr


# In[16]:


arr=np.arange(0.01,1.01,0.01)
arr


# In[17]:


arr.reshape(10,10)


# In[19]:


mat=np.arange(1,26).reshape(5,5)
mat


# In[21]:


mat[2:,1:]


# In[22]:


mat=np.arange(1,26).reshape(5,5)
mat


# In[23]:


mat[:3,1:2]


# In[30]:


mat[1].sum()


# In[29]:


mat.std()


# In[34]:


mat.sum(axis=0)


# In[ ]:




