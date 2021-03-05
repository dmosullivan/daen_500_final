#!/usr/bin/env python
# coding: utf-8

# In[2]:


class My_String:
    def __init__(self):
        self.words = ""
    def get_string(self):
        self.string = input()
    def print_string(self):
        print(self.string.upper())
string = My_String()
string.get_string()
string.print_string()


# In[ ]:




