#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#read in data 
data_url = "https://questionnaire-148920.appspot.com/swe/data.html"
salary_data = pd.read_html(data_url)
#number_of_tables = len(salary_data)
#print(f"Number of tables found: {number_of_tables}")
#create dataframe
salary_data_df = salary_data[0]


# In[3]:


#outputting read data 
display(salary_data_df)


# In[4]:


#count table null values 
#checking for potential corrupted data on columns
null_count = salary_data_df.isnull().sum()
print(null_count)


# In[5]:


salary_data_df['Salary'] = pd.to_numeric(salary_data_df['Salary'].replace('[\$,]','', regex=True), errors='coerce')
salary_data_df.dropna(subset=['Salary'], inplace=True)
salary_data_df['Salary'] = salary_data_df['Salary'].replace('[\$,]','', regex=True).astype(float)
# Calculate the median salary, excluding NaN values
median_salary = salary_data_df['Salary'].median()
# Fill NaN values in the 'Salary' column with the median salary
salary_data_df['Salary'].fillna(median_salary, inplace=True)


# In[6]:


#null_count = salary_data_df.isnull().sum()
#print(null_count)
display(salary_data_df)
most_recent_year = salary_data_df['Year'].max()


# In[7]:


display(salary_data_df.nlargest(125, 'Salary')['Salary'])
top_125_salaries = salary_data_df.nlargest(125, 'Salary')['Salary']
# Calculate the average (mean) manually
contract_offer = top_125_salaries.sum() / len(top_125_salaries)


# In[8]:


print(f"Qualifying Offer: {most_recent_year}: ${contract_offer:,.2f}")


# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


top_125_salaries = salary_data_df.nlargest(125, 'Salary').sort_values(by='Salary', ascending=False)


# In[11]:


top_125_salaries = salary_data_df.nlargest(125, 'Salary').sort_values(by='Salary', ascending=False)


# In[12]:


# Create a line plot using Seaborn
sns.lineplot(data=top_125_salaries['Salary'].reset_index(drop=True))

# Add a horizontal line for the Qualifying Offer
plt.axhline(y=contract_offer, color='r', linestyle='-', label=f'Qualifying Offer: ${contract_offer:,.2f}')

plt.title('Top 125 MLB Player Salaries in {most_recent_year} with Qualifying Offer')
plt.xlabel('Players (Top 125)')
plt.ylabel('Salary')
plt.grid(True)
plt.legend()
plt.show()


# In[ ]:




