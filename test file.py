#!/usr/bin/env python
# coding: utf-8

# ### <a href="http://www.data8.org/sp20/python-reference.html"> Python Reference Link <a>
# 
# Run the cell below so that we can set our modules up
# 

# In[ ]:


import numpy as np
from datascience import *
import math


# In[ ]:


link = "https://raw.githubusercontent.com/humdskyline/data/main/first_class_survey_s2025.csv"
first_survey = Table.read_table(link)
first_survey.show(5)


# ## 1. Write the Python code to find:
# <i>What is the average height of the class?</i>

# In[ ]:





# In[ ]:


#What is the major of the person in the second row?
second_row = first_survey.take(1)
print(second_row)
their_major = second_row.column("Major")
print(their_major)


# In[ ]:


first_survey.group("Class Modality")


# In[ ]:


first_survey.show(5)


# In[ ]:




