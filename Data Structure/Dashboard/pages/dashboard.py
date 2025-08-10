import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px


st.subheader("Titanic Data Data Insights and Visulation ")
st.markdown("Get all the insights as stats and visualizations about the Titanic dataset in this application")

st.subheader("Dataset")

df = sns.load_dataset('titanic')
st.dataframe(df)

#Filters
st.sidebar.header("Filters")

gender = st.sidebar.multiselect('Gender', options=df['sex'].unique())

pclass = st.sidebar.multiselect('Passenger Class', options=df['pclass'].unique())

min_age, max_age = st.sidebar.slider('Age Range', min_value=int(df['age'].min()), max_value=int(df['age'].max()), value=(int(df['age'].min()), int(df['age'].max())))



st.subheader("Visualizations of Insights")


#Age Distribution

fig = px.histogram(df, x='age', title='Age Distribution of Titanic Passengers', color = 'embarked')
st.plotly_chart(fig)
st.markdown("This graph shows the distribution of ages of the people at the titanic ")

fig = px.box(df, x = 'pclass',y='age',color='survived',title='Age wise fare')
st.plotly_chart(fig)


