import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# جلب البيانات من ملف Csv
@st.cache_data
def load_data():
    return pd.read_csv("D:\\dataAnalysisPython\\test\\pro-test4\\student-performance-analysis\\student_performance_data.csv")

data_student = load_data()
print(data_student.head(10))

# معلومات الجدول
print(data_student.info())
    
# ملخص احصائى
print(data_student.describe())


# لمعرفه القيم المفقوده
print(data_student.isnull().sum())


# رسم التوزيع التكرارى ل المعدل التركمى
sns.histplot(data = data_student , x = 'GPA' , kde = True)
plt.axvline(data_student['GPA'].mean() , color = 'red')
plt.axvline(data_student['GPA'].median() , color = 'black')
plt.xlabel('Grade point Average')
plt.ylabel('count')
plt.title('Frequency Distribution GPA')
plt.show()


# معرفه القيم الشاذه
def outliers(df,col):
    q1 = df[col].quantile(0.25)
    q2 = df[col].median()
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lb = q1 - 1.5 * iqr
    ub = q3 + 1.5 * iqr
    outliers = data_student[(data_student[col] < lb )| (data_student[col] > ub)]
    sum_outliers = len(outliers)
    return q1 , q3 , iqr , lb , ub , sum_outliers

outliers(data_student,'GPA')

#  الرسم الصندوقى ل المعدل التركمى 
sns.boxplot(data = data_student , x = 'GPA')
plt.xlabel('Grade point Average')
plt.title('Box plot GPA')
plt.show()

# التحليل الاستكشافى
def top_low_deg(df,col):
    # اعلى 10 درجات
    top_10 = df.nlargest(10,col)
    print(f"\n TOP TEN : \n {top_10}")
    # اعلى درجه
    max_gpa = df[col].max()
    print(f"great gpa : \n {max_gpa}")
    # اقل 10 درجات
    low_10 = df.nsmallest(10,col)
    print(f"\n low TEN : \n {low_10}")
    # اقل درجه
    min_gpa = df[col].min()
    print(f"less gpa : \n {min_gpa}")
    return top_10, max_gpa , low_10 , min_gpa
top_low_deg(data_student,'GPA')

# داله لحساب المتوسط
def mean_gap(cols):
    df = data_student.groupby(cols)['GPA'].mean().sort_values(ascending=True)
    print(f'\n mean {df} :')
    return df
# داله لرسم مخطط الاعمده
def barPlot(x_col,y_col,x_label,y_label,title):
    plt.figure(figsize = (15,5))
    sns.barplot(x =x_col  , y = y_col)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

columns = ['Gender', 'Age','Major', 'PartTimeJob', 'ExtraCurricularActivities']
for col in columns:
    data = mean_gap(col)
    barPlot(data.index, data.values ,col,f'mean {col}', f'avg {col}')


def catplot(col,title):
    sns.catplot(data=data_student, x="Gender", y="GPA", hue=col, kind="bar")
    plt.title(title)
    plt.show()

column = ['Age','Major', 'PartTimeJob', 'ExtraCurricularActivities']
for col in column:
    catplot(col , col)


# داله لمعرفه معامل الارتباط
def correlation_coefficient(col):
    corr = data_student[[col,'GPA']].corr()
    print(f'\n correlation coefficient {corr} :')
    return corr

# داله لرسم مخطط التبعثر
def scatterplot(x_col,y_col):
    sns.scatterplot(data = data_student , y = x_col , x = y_col)
    plt.title(f'scatter plot {x_col} & {y_col}')
    plt.show()

cols = ['AttendanceRate','StudyHoursPerWeek']
for col in cols:
    correlation_coefficient(col)
    scatterplot(col,'GPA')

# داله لرسم خريطه الحراريه
coefficient = data_student[['AttendanceRate','StudyHoursPerWeek','GPA']].corr()
sns.heatmap(data = coefficient[['GPA']] ,annot= True , cmap = 'viridis')
plt.show()





