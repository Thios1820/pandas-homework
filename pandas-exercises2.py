
import pandas as pd
insurance_data = pd.read_csv("insurance.csv")


# 1. In pandas-notebook project do the following exercise in pairs
# 2. Load the insurance.csv in a DataFrame using pandas.
# Explore the dataset using functions like to_string(), columns, index, dtypes, shape, info() and describe()
#

# *to_string()*

# In[2]:


insurance_data.to_string()


# *columns*

# In[3]:


print(insurance_data.columns)


# *index*

# In[4]:


print(insurance_data.index)


# *dtypes*

# In[5]:


print(insurance_data.dtypes)


# *shape*

# In[6]:


print(insurance_data.shape)


# *info()*

# In[7]:


print(insurance_data.info())


# *describe*

# In[8]:


print(insurance_data.describe())


# 3. Print only the column age
#

# In[9]:


print(insurance_data.age)


# 4. Print only the columns age,children and charges

# In[10]:


print(insurance_data[['age', 'children', 'charges']])


# 5. Print only the first 5 lines and only the columns age,children and charges

# In[11]:


print(insurance_data[['age', 'children', 'charges']][:5])


# 6. What is the average, minimum and maximum charges ?

# In[12]:


print("Average: {0}".format(insurance_data.charges.mean()))
print("Minimum: {0}".format(insurance_data.charges.min()))
print("Maximum: {0}".format(insurance_data.charges.max()))


# 7. What is the age and sex of the person that paid 10797.3362. Was he/she a smoker?
# ## 53, Female, non smoker

# In[13]:


# insurance_data[['age','charges']].where(insurance_data.charges>10000)
print(insurance_data[['age', 'sex', 'smoker']][insurance_data['charges']==10797.3362])


# 8. What is the average, minimum and maximum charges ?
# ## 54 years old

# In[14]:


print(insurance_data[['age']][insurance_data['charges']==insurance_data.charges.max()])


# 9. How many insured people do we have for each region?

# In[15]:


print(insurance_data.groupby(['region']).count()[['age']])


# 10. How many insured people are children?
# ## 1338

# In[16]:


print(insurance_data['children'].count())


# 11. What do you expect to be the correlation between charges and age, bmi and children?
# 12. Using the method corr(), check if your assumptions were correct.
#
# ## charges and bmi increase with age and number of children

# In[17]:


print(insurance_data.corr())


