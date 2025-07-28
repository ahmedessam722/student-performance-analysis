import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

@st.cache_data
def load_data():
    return pd.read_csv("D:\\dataAnalysisPython\\test\\pro-test4\\student_performance_data.csv")
data_student = load_data()

# مخطط التوزيع التكرارى ل معدل التركمى
def histplot(df , col):
    st.subheader(" التوزيع التكراري لـ GPA")
    fig1, ax1 = plt.subplots()
    sns.histplot(data=df, x=col, kde=True, ax=ax1)
    ax1.axvline(df['GPA'].mean(), color='red', label='mean')
    ax1.axvline(df['GPA'].median(), color='black', label='median')
    ax1.legend()
    st.pyplot(fig1)

# الرسم الصندوقى ل المعدل التركمى 
def boxplot(df,col):
    st.subheader('الرسم الصندوقى ل GPA :')
    fig2, ax2 = plt.subplots()
    sns.boxplot(data=df, x= col, ax=ax2)
    st.pyplot(fig2)
    st.write('التاكد من عدم وجود قيم شاذه')

# مخطط الاعمده
def st_plot(df,x_label,y_label):
    fig3 , ax3  = plt.subplots()
    sns.barplot(x =df.index  , y = df.values , ax = ax3)
    ax3.set_xlabel(x_label)
    ax3.set_ylabel(y_label)
    st.pyplot(fig3)

# رسم لمقارنه بين متغيرين
def st_cat(col1,col2,col):
    g =  sns.catplot(data=data_student, x=col1, y=col2, hue=col, kind="bar")
    st.pyplot(g.figure)

# مخطط التبعثر
def st_scatter(x_col,y_col):
    fig, ax = plt.subplots()
    sns.scatterplot(data = data_student , y = x_col , x = y_col, ax= ax)
    st.pyplot(fig)

# الخريطه الحراريه 
def coefficient(df):
    st.subheader("الخريطه الحراريه :")
    coefficient = df[['AttendanceRate','StudyHoursPerWeek','GPA']].corr()
    fig, ax = plt.subplots()
    sns.heatmap(data = coefficient[['GPA']] ,annot= True , cmap = 'viridis' , ax = ax)
    st.pyplot(fig)
