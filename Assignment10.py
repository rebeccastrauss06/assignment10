import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Housing Data (1990) by Rebecca Strauss')
df = pd.read_csv('housing.csv')
df.head()

hp_filter = st.slider('Median House Value:',0,500001,200000)

st.subheader('See more filters in the sidebar:')
st.map(df)

location_filter = st.sidebar.multiselect(
    'Choose Location',
    df.ocean_proximity.unique(),
    df.ocean_proximity.unique())

df = df[df.median_income >= hp_filter]
df = df[df.ocean_proximity.isin(location_filter)]

income_filter = st.sidebar.radio(
    'Choose Income Level',
    ('Low', 'Medium', 'High'))

if income_filter == 'Low':
    df=df[df.median_income <= 2.5]
elif income_filter == 'Medium':
    df=df[(df.median_income > 2.5) & (df.median_income < 4.5)]
elif income_filter == 'High':
    df = df[df.median_income >= 4.5]

st.subheader('Histogram of the Median House Value')

fig, ax = plt.subplots()
df.median_house_value.hist(ax=ax,bins=30)
st.pyplot(fig)