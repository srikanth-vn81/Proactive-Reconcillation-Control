#!/usr/bin/env python
# coding: utf-8

# In[1]:


# data analysis and wrangling
import numpy as np
import pandas as pd
import streamlit as st

# In[3]:


df = pd.read_csv(r"C:\Users\srikanthve\Downloads\Soshan\stylereco.csv")


# In[4]:


head = df.head()


# In[ ]:
st.write(head)



