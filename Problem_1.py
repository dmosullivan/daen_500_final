#!/usr/bin/env python
# coding: utf-8

# In[2]:


lower = int(input("Enter lower range limit:"))
upper = int(input("Enter upper range limit:"))
for i in range(lower, upper+1):
   if((i%7==0) and (i%5!=0)):
      print(i)


# In[ ]:




