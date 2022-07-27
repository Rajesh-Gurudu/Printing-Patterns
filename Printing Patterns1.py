#!/usr/bin/env python
# coding: utf-8

# In[25]:


for i in range(4):
    for j in range(4):
        print('*',end='')
    print()
        


# In[27]:


for i in range(4):
    for j in range(i+1):
        print('#',end='')
    print()


# In[30]:


for i in range(4):
    for j in range(i):
        print('#',end='')
    print()


# In[35]:


for i in range(4):
    for j in range(4-i):
        print('#',end='')
    print()


# In[38]:


for i in range(4):
    for j in range(4+i):
        print('#',end='')
    print()


# In[41]:


for i in range(4):
    for j in range(4+i):
        print('*',end='')
    print()


# In[ ]:




