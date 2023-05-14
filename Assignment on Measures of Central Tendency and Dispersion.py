#!/usr/bin/env python
# coding: utf-8

# # Assignment on Measures of Central Tendency and Dispersion

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


stud=pd.read_csv(r'C:\Users\sreejayan\Desktop\assignment\StudentsPerformance.csv')


# In[3]:


stud.head(50)


# In[4]:


stud.describe()


# In[5]:


# Count the number of males and females
num_males = (stud['gender'] == 'male').sum()
num_females = (stud['gender'] == 'female').sum()

print(f"Number of males: {num_males}")
print(f"Number of females: {num_females}")


# # 1. Find out how many males and females participated in the test.

# In[6]:


num_males = ((stud['gender'] == 'male') & (stud['test preparation course'] == 'completed')).sum()
num_females = ((stud['gender'] == 'female') & (stud['test preparation course'] == 'completed')).sum()
print("number of males",num_males)
print("number of females",num_females)


# # 2. What do you think about the students' parental level of education?

# In[7]:


parental_education_counts = stud["parental level of education"].value_counts()
print(parental_education_counts)


# In[8]:


parental_education_counts.plot(kind="bar")
plt.title("Distribution of Parental Education Levels")
plt.xlabel("Education Level")
plt.ylabel("Count")
plt.show()


# # 3. Who scores the most on average for math, reading and writing based on
# ● Gender
# ● Test preparation course

# In[9]:


# Group the data by gender and calculate the mean scores for each subject
mean_scores = stud.groupby(['gender','test preparation course'])['math score', 'reading score', 'writing score'].mean()
print(mean_scores)


# # 4. What do you think about the scoring variation for math, reading and writing based on
# ● Gender
# ● Test preparation course

# In[10]:


# Group the data by gender and test preparation course, and calculate the VARIANCE scores for each subject
var_scores = stud.groupby(['gender', 'test preparation course'])['math score', 'reading score', 'writing score'].var()
# Print the variance
print(var_scores)


# # 5. The management needs your help to give bonus points to the top 25% of students based on their math score, so how will you help the management to achieve this.

# In[11]:


# Sort the data by math score in descending order
sorted_data = stud.sort_values(by='math score', ascending=False)

# Calculate the 25th percentile of the math scores
math_25_percentile = np.percentile(stud['math score'], 25)

# Create a new column to indicate whether each student is in the top 25% based on their math score
sorted_data['top_25_math'] = sorted_data['math score'] >= math_25_percentile

# Assign bonus points to the students who are in the top 25% based on their math score
sorted_data.loc[sorted_data['top_25_math'], 'math score'] += 10

# Print the updated data frame with bonus points
print(sorted_data)


# In[12]:


sorted_data.head(50)


# In[13]:


stud["math score"].quantile(0.75)
top25=stud[stud["math score"]>=77].sort_values("math score",ascending=False)
top25


# In[ ]:




