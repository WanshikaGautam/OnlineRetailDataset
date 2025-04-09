import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\Dell\Downloads\Online Retail.csv')
#printing first dew rows of the dataset
print(" \n FIRST 10NROWS OF THE DATA SET ARE: \n",df.head(10))

#Shape of the dataset is
print("\n Shape of dataset\n ",df.shape)
#Uniques values in the dataset are

print("\n Unique value in dataset \n ",df.nunique())

#1. CLEANING DATASET

#Removing canceled transactions (InvoiceNo starting with 'C')
canceled_transactions=df[df['InvoiceNo'].astype(str).str.startswith('C')]
print("\n Removed canceled transcations are \n",canceled_transactions)

#Dropping rows with missing CustomerID
rows_dropped=df.dropna(subset=['CustomerID'])
print("Dropping rows with missing customerID \n",rows_dropped)

#Handle negative/zero quantities or prices
values=df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
print("Handling negative or zero Quantities or prices \n",values)

#Filtering out rows where Quantity or unitprice is less than zero
Filtered_value = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
print("Rows where Quantity or unitprice is less than zero: \n",Filtered_value)

#Converting InvoiceDate to datetime format
df['InvoiceDate']=pd.to_datetime(df['InvoiceDate'])
print("InvoiceDate to datetime format :\n",df['InvoiceDate'])

#Creating TotalPrice Column
df['TotalPrice']=df['Quantity']*df['UnitPrice']
print("TotalPrice : \n",df['TotalPrice'])