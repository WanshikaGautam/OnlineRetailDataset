import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
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

#Checking and treating duplicates
print("duplicates value are: \n",df.duplicated().sum())
removed_values=df.drop_duplicates(inplace=True)
print("After removing duplicated values are : \n",removed_values)

#Save treated dataset
df.to_csv("Treated_Online_Retail.csv", index=False)

# EDA (Exploratiry Data Analysis)

#  Displaying the information of the data set
print("Information of the dataset is: \n",df.info())
#Displaying sumarry statics of the data
print("Summary statitics of the numerical data : \n",df.describe())

#Check for the missing values
print("Missing values in the dataset are: \n",df.isnull().sum())
#Check for overall Missing values in the data set
print("Overall missing values in the dataset are: \n",df.isnull().sum().sum())

# Handling missing values for description coloumn
df.fillna({'Description': 'Unknown'}, inplace=True)
#handling missing values for customer coloumn
df = df.dropna(subset=['CustomerID'])

#After handling missing values 
print("After handling missing values : \n",df.isnull().sum())
#Check for unique values
print("\n Unique Values in each coloumn: \n",df.nunique())

#Compute corelation
# corr for corelation
correlation_matrix=df.corr(numeric_only=True)

#check for outliers
plt.figure(figsize=(14, 6))
sns.boxplot(y=df['Quantity'], color='skyblue')
plt.title('Box Plot of Quantity', fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.show()
# box plot for unit price
sns.boxplot(y=df['UnitPrice'], color='lightgreen')
plt.title('Box Plot of UnitPrice', fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.show()

#treating outliers
def remove_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

# Remove outliers from Quantity and UnitPrice
cleaned_df = remove_outliers_iqr(df, 'Quantity')
cleaned_df = remove_outliers_iqr(cleaned_df, 'UnitPrice')

# Creating  box plots
plt.figure(figsize=(14, 6))

# Box plot before outlier removal
plt.subplot(1, 2, 1)
sns.boxplot(data=df[['Quantity', 'UnitPrice']], palette="Set2")
plt.title('Before Outlier Removal', fontsize=14)
plt.grid(True)

# Box plot after outlier removal
plt.subplot(1, 2, 2)
sns.boxplot(data=cleaned_df[['Quantity', 'UnitPrice']], palette="Set3")
plt.title('After Outlier Removal', fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.show()

# diaplay the correlation matrix as heatmap
plt.figure(figsize=(8,6))
sns.heatmap(correlation_matrix, annot= True, cmap="Blues", fmt=".2f",linewidths=0.8) #coolwarm,
plt.title("correlation Heatmap")
plt.show()

#Top 10 countries by Total Revenue
top_customers = df.groupby('CustomerID')['TotalPrice'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Customers by Total Revenue:\n", top_customers)

#Total Number of Unique Products Sold 
unique_products = df['Description'].nunique()
print("\nTotal Unique Products Sold:", unique_products)

# Showing Monthly Sales Trend 
df['Month'] = df['InvoiceDate'].dt.to_period('M')
monthly_sales = df.groupby('Month')['TotalPrice'].sum()
print("\nMonthly Sales Trend:\n", monthly_sales)

# Most Frequently Purchased Item 
most_frequent = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(1)
print("\nMost Frequently Purchased Item:\n", most_frequent)

# Peak Hours of the Day 
df['Hour'] = df['InvoiceDate'].dt.hour
hourly_transactions = df['Hour'].value_counts().sort_index()
print("\nPeak Hours of the Day:\n", hourly_transactions)

#Frequent & High-Spending Customers 
frequent_customers = df['CustomerID'].value_counts().head(10)
print("\nMost Frequent Customers:\n", frequent_customers)

# High-spending = highest total revenue
high_spenders = df.groupby('CustomerID')['TotalPrice'].sum().sort_values(ascending=False).head(10)
print("\nTop High-Spending Customers:\n", high_spenders)

#Country-wise Revenue & Transaction Count 
country_revenue = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False)
country_transactions = df['Country'].value_counts()

# Time of Day with Highest Sales
df['Hour'] = df['InvoiceDate'].dt.hour
hourly_sales = df.groupby('Hour')['TotalPrice'].sum()

#Proportion of Orders from Top 5 Countries 
country_counts = df['Country'].value_counts()
top5_orders = country_counts.head(5)
others = country_counts[5:].sum()
top5_orders['Others'] = others
print("\nProportion of Orders from Top 5 Countries:\n", top5_orders)

#Hour vs Day of Week Sales 
df['Hour'] = df['InvoiceDate'].dt.hour
df['DayOfWeek'] = df['InvoiceDate'].dt.day_name()

order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']  # Fix

heatmap_data = df.groupby(['DayOfWeek', 'Hour'])['TotalPrice'].sum().unstack().reindex(order)
heatmap_data = df.groupby(['DayOfWeek', 'Hour'])['TotalPrice'].sum().unstack().reindex(order).fillna(0)
print("\nHour vs Day of Week Sales:\n", heatmap_data)



#Save treated dataset
df.to_csv("Treated_Online_Retail.csv", index=False)

# 3. Visualization 

# Plotting monthly sales
monthly_sales.plot(kind='line', figsize=(10, 5), title="Monthly Sales Trend", marker='H')
plt.ylabel("Total Revenue")
plt.xlabel("Month")
plt.grid(True)
plt.show()

# Plotting peak hours
hourly_transactions.plot(kind='bar', figsize=(10, 5), color='seagreen', title="Peak Hours of Transactions")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Transactions")
plt.show()

# Bar plot: Top 10 countries by transaction count
country_transactions.head(10).plot(kind='bar', title="Top 10 Countries by Transaction Count", color='purple', figsize=(10, 4))
plt.ylabel("Transactions")
plt.show()

# Plot hourly sales

hourly_sales.plot(kind='bar', title="Sales by Hour of Day", color='crimson', figsize=(10, 4))
plt.ylabel("Total Revenue")
plt.xlabel("Hour of Day")
plt.show()


# Customer Purchase Distribution
plt.figure(figsize=(10, 5))
customer_totals = df.groupby('CustomerID')['TotalPrice'].sum()
sns.histplot(customer_totals, bins=50, kde=True, color='mediumseagreen')
plt.title("Customer Purchase Distribution")
plt.xlabel("Total Purchase Amount")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

#Hour vs Day of Week Sales 
plt.figure(figsize=(14, 6))
sns.heatmap(heatmap_data, cmap='YlGnBu', linewidths=0.3, annot=True)
plt.title("Sales Heatmap: Hour of Day vs Day of Week", fontsize=16)
plt.xlabel("Hour of Day")
plt.ylabel("Day of Week")
plt.tight_layout()
plt.show()
#Histogram: Distribution of Order Quantities
plt.figure(figsize=(10, 5))
sns.histplot(df['Quantity'], bins=100, kde=True, color='dodgerblue')
plt.xlim(-20, 100)  # limit x-axis to reduce skew from extreme outliers
plt.title("Distribution of Order Quantities")
plt.xlabel("Quantity")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.show()

# Proportion of Orders from Top 5 Countries 
plt.figure(figsize=(7, 7))
top5_orders.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title("Order Proportion: Top 5 Countries")
plt.ylabel("")
plt.tight_layout()
plt.show()




