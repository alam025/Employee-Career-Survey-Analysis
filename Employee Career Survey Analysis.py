#!/usr/bin/env python
# coding: utf-8

# # Employee Career Survey Analysis

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# In[2]:


data=pd.read_csv(r"Downloads\python day 24 Your Career Aspirations of GenZ.csv")


# In[3]:


data.head()


# In[4]:


data.columns


# In[5]:


country=data['Your Current Country.'].value_counts()
label=country.index
counts=country.values
colors=['red','lightgreen']
fig=go.Figure(data=[go.Pie(labels=label,values=counts)])
fig.update_layout(title_text="Current Country")
fig.update_traces(hoverinfo='label+value',textinfo='percent',textfont_size=30,marker=dict(colors=colors,line=dict(color='black',width=3)))
fig.show()


# In[6]:


country


# # Factor influencing career aspirations

# In[17]:


data.head()


# # Which of the below factors influence the most about your career aspirations ?

# In[33]:


ques1="Which of the below factors influence the most about your career aspirations ?"
ques1=data[ques1].value_counts()
label=ques2.index
counts=ques2.values
colors=['lightgreen','hotpink']
fig=go.Figure(data=[go.Pie(labels=label,values=counts)])

fig.update_layout(title_text="Which of the below factors influence the most about your career aspirations ")
fig.update_traces(hoverinfo='label+value',textinfo='percent',textfont_size=30,marker=dict(colors=colors,line=dict(color='black',width=3)))
fig.show()


# # Would you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it.

# In[11]:


ques2="Would you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it."
ques2=data[ques2].value_counts()
label=ques2.index
counts=ques2.values
colors=['orange','black']
fig=go.Figure(data=[go.Pie(labels=label,values=counts)])

fig.update_layout(title_text="Would you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it.")
fig.update_traces(hoverinfo='label+value',textinfo='percent',textfont_size=30,marker=dict(colors=colors,line=dict(color='black',width=3)))
fig.show()


# In[12]:


ques2


# In[ ]:





# # How likely is that you will work for one employer for 3 years or more ?

# In[13]:


ques3="How likely is that you will work for one employer for 3 years or more ?"
ques3=data[ques3].value_counts()
label=ques3.index
counts=ques3.values
colors=['aqua','red']
fig=go.Figure(data=[go.Pie(labels=label,values=counts)])

fig.update_layout(title_text="How likely is that you will work for one employer for 3 years or more")
fig.update_traces(hoverinfo='label+value',textinfo='percent',textfont_size=30,marker=dict(colors=colors,line=dict(color='black',width=3)))
fig.show()


# In[14]:


ques3


# In[ ]:





# # What is the most preferred working environment for you.

# In[15]:


ques5='What is the most preferred working environment for you.'
ques5=data[ques5].value_counts()
label=ques5.index
counts=ques5.values
colors=['green','magenta']
fig=go.Figure(data=[go.Pie(labels=label,values=counts)])

fig.update_layout(title_text="How likely is that you will work for one employer for 3 years or more")
fig.update_traces(hoverinfo='label+value',textinfo='percent',textfont_size=30,marker=dict(colors=colors,line=dict(color='black',width=3)))
fig.show()


# In[16]:


ques5.count


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




