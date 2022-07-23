#!/usr/bin/env python
# coding: utf-8

# In[1]:


# data analysis and wrangling
import numpy as np
import pandas as pd
import streamlit as st

# In[3]:
uploaded_file = st.file_uploader(
        "",key="1",
        help="To activate 'wide mode', go to the hamburger menu > Settings > turn on 'wide mode'",)

if uploaded_file is not None:
	file_container = st.expander("Check your uploaded .xlsx")
	shows = pd.read_csv(uploaded_file)
	
	uploaded_file.seek(0)

	st.write(shows.head())
	
else:
	st.write("")
	

	
        
# In[4]:




# In[ ]:




