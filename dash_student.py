import streamlit as st
import pandas as pd
from students import outliers, top_low_deg, mean_gap, correlation_coefficient
from visuals import histplot, boxplot, st_plot, st_cat, st_scatter, coefficient


@st.cache_data
def load_data():
    return pd.read_csv(
        "D:\\dataAnalysisPython\\test\\pro-test4\\student_performance_data.csv"
    )


data_student = load_data()


# عنوان الصفحه
st.title("لوحة تحليل أداء الطلاب")

section = st.sidebar.radio(
    "انتقل إلى:",
    (
        "مقدمة وبيانات الجدول",
        "تحليل الدرجات",
        "المتوسط على الجنس",
        "المتوسط على العمر",
        "المتوسط على التخصص الدراسى",
        "المتوسط حسب وظيفه بدوام جزئى",
        " المتوسط حسب الانشطه الامنهجيه",
        "معاملات الارتباط",
    ),
)

if section == "مقدمة وبيانات الجدول":
    st.header("مقدمه :")
    st.write("الهدف هو تحليل اداء الطلاب")
    st.write(
        "الجدول عباره عن 500 صف و الاعمده : ['Gender', 'Age','Major', 'PartTimeJob', 'ExtraCurricularActivities', 'AttendanceRate', 'StudyHoursPerWeek']"
    )
    st.subheader("اول 10 صفوف من الجدول :")
    st.dataframe(data_student.head(10))

    with st.expander("ملخص احصائى"):
        st.write(data_student.describe())
    st.write("التاكد من عدم وجود قيم مفقوده")
    with st.expander("القيم المفقودة"):
        st.write(data_student.isnull().sum())

    histplot(data_student, "GPA")

    sum_outliers, q1,q3, iqr, lb, ub = outliers(data_student, "GPA")
    st.write(f"الربع الاول = {q1}")
    st.write(f"الربع الثالث = {q3}")
    st.write(f"المدى الربيعى= {iqr}")
    st.write(f"الحد الادنى = {lb}")
    st.write(f"الحد الاقصى = {ub}")
    st.write(f" عدد القيم الشاذه = {sum_outliers}")

    boxplot(data_student, "GPA")


if section == "تحليل الدرجات":
    top_10, max_gpa, low_10, min_gpa = top_low_deg(data_student, "GPA")
    st.subheader("اعلى 10 درجات : ")
    st.dataframe(top_10)

    st.write(f"اعلى درجه : {max_gpa}")

    st.subheader("اقل 10 درجات : ")
    st.dataframe(low_10)
    st.write(f"اقل درجه : {min_gpa}")


if section == "المتوسط على الجنس":
    st.subheader("المتوسط حسب الجنس :")
    st.dataframe(mean_gap("Gender"))

    data1 = mean_gap("Gender")
    st.subheader("رسم مخطط الاعمده :")
    st_plot(data1, "gender", "mean gender")
    st.write("المعدل التركمى بين الذكور و الاناث متسوى")

    st.subheader("رسم مخطط تحليل البيانات تصنيفه على حسب العمر :")
    st_cat("Gender", "GPA", "Age")
    st.write(
        "الذكور الذين يبلغون من العمر 23 عام حصلو على اعلى معدل  و الذكور الذين يبلغون من العام 18 عام حصلو على اقل معدل"
    )
    st.write(
        "الاناث الذين يبلغون من العمر 21 عام حصلو على اعلى معدل  و الاناث الذين يبلغون من العام 18 عام حصلو على اقل معدل"
    )

    st.subheader("رسم مخطط تحليل البيانات تصنيفه على حسب التخصص الدراسى :")
    st_cat("Gender", "GPA", "Major")
    st.write(
        "الذكور الذين التحقو فى تخصص الهندسه و الفنون حصلو على اعلى معدل والذكور الذين التحقو فى تخصص علوم حصلو على اقل معدل"
    )
    st.write(
        "الاناث الذبن التحقو فى تخصص الاعمال حصلو على اعلى معدل و الاناث الذين التحقو فى فى تخصص الهندسه حصلو على اقل معدل"
    )

    st.subheader("رسم مخطط تحليل البيانات تصنيفه على حسب وظيفه بدوام جزئى :")
    st_cat("Gender", "GPA", "PartTimeJob")
    st.write(
        "الذكور الذين يعملون فى وظيفه يدوام جزئى حصلو على معدل اعلى و الاناث الذين يعملون فى وظيفه بدوام جزئى حصلو على معدل اعلى"
    )

    st.subheader("رسم مخطط تحليل البيانات تصنيفه على حسب الانشطه اللامنهجيه :")
    st_cat("Gender", "GPA", "ExtraCurricularActivities")
    st.write(
        "الذكور الذين اشتركو فى الانشطه اللامنهجيه حصلو على معدل اعلى و الاناث الذين اشتركو فى الانشطه اللامنهجيه حصلو على معدل اعلى"
    )

if section == "المتوسط على العمر ":
    st.subheader(" المتوسط حسب العمر :")
    st.dataframe(mean_gap("Age"))
    st.write(
        "الطلاب الذين يبلغون من العمر 23 عام حلو على اعلى معدل و الطلاب الذين يبلغون من العمر 18 حصلو على اقل معدل"
    )

    st.subheader("رسم مخطط الاعمده :")
    data1 = mean_gap("Age")
    st_plot(data1, "Age", "mean Age")

if section == "المتوسط على التخصص الدراسى":
    st.subheader(" المتوسط حسب التخصص الدراسى:")
    st.dataframe(mean_gap("Major"))
    st.write(
        "الطلاب الذبن التحقو فى تخصص الاعمال حصلو على اعلى معدل و الطلاب الذبن التحقو فى تخصص التعليم حصلو على اقل معدل"
    )

    st.subheader("رسم مخطط الاعمده :")
    data1 = mean_gap("Major")
    st_plot(data1, "Major", "mean Major")

if section == "المتوسط حسب وظيفه بدوام جزئى":
    st.subheader(" المتوسط حسب وظيفه بدوام جزئى:")
    st.dataframe(mean_gap("PartTimeJob"))
    st.write("الطلاب الذين يعمالون فى وظيفه يدوام جزئى حصلو على معدل اعلى")

    st.subheader("رسم مخطط الاعمده :")
    data1 = mean_gap("PartTimeJob")
    st_plot(data1, "PartTimeJob", "mean PartTimeJob")

if section == " المتوسط حسب الانشطه الامنهجيه":
    st.subheader(" المتوسط حسب الانشطه الامنهجيه:")
    st.dataframe(mean_gap("ExtraCurricularActivities"))
    st.write("الطلاب الذين اشتركو فى الانشطه الامنهجيه حصلو على معدل اعلى")

    st.subheader("رسم مخطط الاعمده :")
    data1 = mean_gap("ExtraCurricularActivities")
    st_plot(data1, "ExtraCurricularActivities", "mean ExtraCurricularActivities")


if section == "معاملات الارتباط":
    st.subheader("معامل الارتباط بين المعدل التركمى و ساعات الدراسه فى الاسبوع :")
    corr = correlation_coefficient("StudyHoursPerWeek")
    st.dataframe(corr)
    st.subheader("مخطط التبعثر :")
    st_scatter("StudyHoursPerWeek", "GPA")

    st.subheader("معامل الارتباط بين المعدل التركمى و الحضور:")
    corr2 = correlation_coefficient("AttendanceRate")
    st.dataframe(corr2)
    st.subheader("مخطط التبعثر :")
    st_scatter("AttendanceRate", "GPA")

    coefficient(data_student)
