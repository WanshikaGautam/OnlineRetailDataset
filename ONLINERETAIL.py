import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#importing dataset 
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


