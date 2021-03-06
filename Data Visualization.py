# -*- coding: utf-8 -*-
"""Data Visualization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NS9NcSh3P54vtygwpBcg7ukD2lRjL_6P

# Import Library
"""

import pandas as pd, numpy as np
import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/gdrive')

"""# Load Dataset"""

path_1 = '/content/gdrive/MyDrive/Colab Notebooks/Dataset Latihan/order_details.csv'
path_2 = '/content/gdrive/MyDrive/Colab Notebooks/Dataset Latihan/order_lists.csv'

details = pd.read_csv(path_1)
lists = pd.read_csv(path_2)

dataset = pd.merge(details, lists, how='right', on='order_id')
dataset.head()

"""# Check Data"""

# Missing Value
dataset.isnull().sum()

# Duplicated Value
dataset.duplicated().sum()

dataset = dataset.dropna()

dataset = dataset.drop_duplicates()

"""# Bar Chart"""

segment_cost = dataset.groupby(['segment']).sum()['sales']

plt.bar(segment_cost.index, segment_cost)
plt.show()

country_sales = dataset.groupby(['country']).sum()['sales']

plt.figure(figsize=(20, 7))
plt.bar(country_sales.index, country_sales)
plt.show()

"""# Pie Chart"""

ship_count = dataset.groupby(['ship_mode']).count()['order_id']

plt.pie(ship_count, labels=ship_count.index, autopct='%1.0f%%')
plt.show()

"""# Histogram"""

plt.title('Profit Distribution')
plt.hist(dataset['profit'])
plt.show()

q1 = np.quantile(dataset['profit'], 0.25, axis=0)
q3 = np.quantile(dataset['profit'], 0.75, axis=0)

iqr = (q3 - q1) * 1.5
lower = q1 - iqr
upper = q3 + iqr

profit = dataset.loc[(dataset['profit'] > lower) & (dataset['profit'] < upper), 'profit']

plt.title('Profit Distribution')
plt.hist(profit)
plt.show()

"""# Distribution/Density Plot"""

dataset['profit'].plot.density()
plt.show()

profit.plot.density()
plt.show()

dataset.groupby('country')['profit'].plot.density()
plt.show()

"""# Line Chart"""

dataset.head()

# https://www.journaldev.com/23365/python-string-to-datetime-strptime

dataset.order_date = pd.to_datetime(dataset.order_date, format='%m/%d/%Y')
dataset.ship_date = pd.to_datetime(dataset.ship_date, format='%m/%d/%Y')

time_series = dataset.groupby(['order_date']).sum()['sales'].reset_index()
time_series = time_series.loc[(time_series['order_date']>='2014-01-01') & (time_series['order_date']<='2014-12-31')]

plt.figure(figsize=(20, 7))
plt.title('Sales in January')
plt.plot(time_series.order_date, time_series.sales)
plt.show()

time_series['order_dow'] = time_series['order_date'].dt.dayofweek

dow = time_series.groupby(['order_dow']).mean()['sales']

plt.figure(figsize=(15, 4))
plt.title('Sales in 2014')
plt.plot(dow.index, dow)
plt.show()

"""# Seaborn"""

import seaborn as sns
dataset.head()

"""# Bar Chart"""

sns.countplot(data=dataset, x='category')
plt.show()

sns.barplot(data=dataset, x='category', y='profit', estimator=np.mean
            , order=['Office Supplies', 'Technology', 'Furniture'])
plt.show()

"""# Scatter Plot"""

sns.scatterplot(data=dataset, x='sales', y='Cost', hue='category')
plt.show()

"""# Heatmap Chart"""

data_corr = dataset[['profit', 'Cost', 'sales', 'quantity']].corr(method='spearman')

plt.figure(figsize=(12, 9))
plt.title('Correlation')
sns.heatmap(data_corr, annot=True)
plt.show()

"""# Violin Plot"""

plt.figure(figsize=(12, 9))
sns.violinplot(data=dataset, y='quantity', x='ship_mode')
plt.show()

"""# Swarmplot"""

plt.figure(figsize=(12, 9))
sns.swarmplot(data=dataset.sample(frac=0.03), y='Cost', x='ship_mode')
plt.show()

"""# Boxplot"""

plt.figure(figsize=(12, 9))
sns.boxplot(data=dataset, y='quantity', x='category')
plt.show()

numerical = dataset[['category','profit', 'Cost', 'sales', 'quantity']]

sns.pairplot(numerical, hue='category')
plt.show()

"""# Customization Chart

# Subplot
"""

plt.figure(figsize=(20, 7))
plt.subplot(1, 3, 1)
sns.regplot(x='sales', y='Cost', data=dataset)

plt.subplot(1, 3, 2)
sns.regplot(x='profit', y='Cost', data=dataset)

plt.subplot(1, 3, 3)
sns.scatterplot(x='sales', y='Cost', size='quantity', data=dataset)

plt.show()

def hist_viz(dataset, columns, dim, size=(15, 15)):
    i = 1
    plt.figure(figsize=size)
    for col in columns:
        plt.subplot(dim[0], dim[1], i)
        sns.histplot(data=dataset, x=col)
        i = i + 1
    plt.show()

hist_viz(dataset=dataset, columns=['profit', 'Cost', 'sales', 'quantity'], dim=[2, 2])

"""# Legend and Label"""

plt.title('Relationship between Profit and Cost')
sns.scatterplot(x='profit', y='Cost', hue='category', data=dataset)
plt.xlabel('Profit per Product')
plt.ylabel('Cost per Product')
#Change Legend
plt.legend({'Furniture', 'Office Supplies', 'Technology'})
plt.show()

"""# Color"""

sns.countplot(data=dataset, x='ship_mode', palette=['blue','yellow','red'], hue='category')
plt.show()

"""# SweetViz"""

!pip install sweetviz

import sweetviz as sv

my_report = sv.analyze(dataset[['profit', 'sales', 'Cost', 'quantity']].sample(frac=0.2))

my_report.show_notebook()

country = dataset.loc[dataset.country.isin(['Germany', 'United Kingdom'])]
sns.countplot(y='country', data=country, order=['Germany', 'United Kingdom'], palette=['Red', 'yellow'])
plt.show()
# country['country'].value_counts().index

"""# Plotly Express"""

import plotly.express as px

fig = px.violin(dataset, y='sales', x='ship_mode')
fig.show()

country = dataset.groupby(['country']).sum()['quantity'].reset_index()
px.bar(country, x='country', y='quantity').show()

"""# Folium"""

import folium

dataset.head()

m = folium.Map(location=[49.006890, 8.403653])
m