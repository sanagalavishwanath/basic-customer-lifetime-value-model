#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import warnings
warnings.filterwarnings("ignore")
df=pd.read_csv(r"C:\Users\sanagalakumudini\Downloads\Ecommerce_Data-1.csv")
df.head()


# In[17]:


df["revenue"]=df["Quantity"]*df["UnitPrice"]
df.drop("Unnamed: 0",axis=1,inplace=True)
df["Date"]=pd.to_datetime(df["Date"])
df=df[df["Quantity"]>0]
df.head()


# In[18]:


max_date=df["Date"].max()
df2=df.groupby("CustomerID").agg(
{
    "Date":lambda x:(max_date-x.min()).days,
    "InvoiceNo": lambda x:len(x),
    "Quantity":lambda x :x.sum(),
    "revenue":lambda x:x.sum()})
df2


# In[30]:


def customer_model(data):
    max_date=df["Date"].max()
    data=data.groupby("CustomerID").agg(
{
    "Date":lambda x:(max_date-x.min()).days,
    "InvoiceNo": lambda x:len(x),
    "Quantity":lambda x :x.sum(),
    "revenue":lambda x:x.sum()})
    return data
data=customer_model(df)
data.head()


# In[32]:


#chnage the name of the coloumns and ensure that we dont have 0 quantity
data.columns=["age","num_transactions","quantity","revenue"]
data=data[data["quantity"]>0]
data.head()


# In[33]:


data["AOV"]=data["revenue"]/data["num_transactions"]
data


# In[34]:


purchase_freq=sum(data["num_transactions"])/len(data)
purchase_freq


# In[35]:


repeat_rate=data[data["num_transactions"]>1].shape[0]/data.shape[0]
repeat_rate


# In[36]:


churn_rate=1-repeat_rate
churn_rate


# In[37]:


data["profit_margin"]=data["revenue"]%10


# In[38]:


data


# In[39]:


data["cltv"]=((data["AOV"]*purchase_freq)/churn_rate)*10


# In[40]:


data


# In[41]:


print("the median CLTV is",data["cltv"].median())
print("the avergae CLTV is ",data["cltv"].mean())


# In[42]:


data.sort_values(by="cltv").reset_index()


# In[ ]:




