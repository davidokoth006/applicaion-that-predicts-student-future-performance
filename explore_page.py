import streamlit as st
import pandas as pd
import matplotlib as plt
import plotly.express as px
import pygwalker as pyg
from PIL import Image

# @st.cache_data

# def load_data():
#     df = pd.read_csv("Student_Performance.csv")
#     df = df[["Hours_Studied", "Previous_Scores","Extracurricular_Activities","Sleep_Hours","Performance_Index","Students_Attendance", "Target"]]
#     df = df.dropna()
#     df.isnull().sum()
#     df = df.drop("Extracurricular_Activities", axis = 1)
#     df = df[df["Performance_Index"]<= 70]
#     df = df[df["Performance_Index"]>= 45]
#     df = df[df["Target"] != 'other']
#     return df

# df = load_data()

def show_explore_page():
    

#     data = df["Performance_Index"].value_counts()
#     fig1, ax1 =plt.subplots()
#     ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
#     ax1.axis("equal") #equal ensure pie is drawn as a circle

#     st.write("Number of data for different students")

#     st.pyplot(fig1)


    df = pd.read_excel(
        io = 'performance.xlsx',
        engine = 'openpyxl',
        sheet_name = 'performance',
        skiprows=0,
        usecols='A:Q',
        nrows=481,
    )

    
    # st.dataframe(df)
    #--------SIDEBAR -----------
    gender =st.sidebar.multiselect(
        "Explore Select Gender",
        options=df["gender"].unique(),
        default=df["gender"].unique()
    )

    Nationality =st.sidebar.multiselect(
        "Select Nationality",
        options=df["Nationality"].unique(),
        default=df["Nationality"].unique()
    )

    topic =st.sidebar.multiselect(
        "Select Topic",
        options=df["Topic"].unique(),
        default=df["Topic"].unique()
    )

    semester =st.sidebar.multiselect(
        "Select Semester",
        options=df["Semester"].unique(),
        default=df["Semester"].unique()
    )

    # raisedhands =st.sidebar.multiselect(
    #     "Select Raised Hands",
    #     options=df["raisedhands"].unique(),
    #     default=df["raisedhands"].unique()
    # )

    parentrssatifaction =st.sidebar.multiselect(
        "Select Parent School Satisfaction",
        options=df["ParentschoolSatisfaction"].unique(),
        default=df["ParentschoolSatisfaction"].unique()
    )

    studentsAbsentDays =st.sidebar.multiselect(
        "Select Student Absent Days",
        options=df["StudentAbsenceDays"].unique(),
        default=df["StudentAbsenceDays"].unique()
    )

    StageID =st.sidebar.multiselect(
        "Select StageID",
        options=df["StageID"].unique(),
        default=df["StageID"].unique()
    )


    df_selection = df.query(
        "gender == @gender & Nationality ==@Nationality & Topic ==@topic & Semester ==@semester & ParentschoolSatisfaction ==@parentrssatifaction & StudentAbsenceDays == @studentsAbsentDays & StageID == @StageID"
    )

    # st.dataframe(df_selection)


    # ------MAIN PAGE
    st.title(":bar_chart: Student Performance")
    st.markdown("##")

    total_discusion = int(df_selection["Discussion"].sum())
    total_raisehands = df_selection["raisedhands"].sum()
    average_rasisehands_per_student = round(df_selection["raisedhands"].mean(), 2)
    average_discussion_per_student = round(df_selection["Discussion"].mean(), 2)

    st.markdown("---")

    lfcol, mdlcol, rtcol, othercol = st.columns(4)
    with lfcol:
        st.write("Total Discussions")
        st.subheader(total_discusion)

    with mdlcol:
        st.write("Average Discussions")
        st.subheader(average_discussion_per_student)

    with rtcol:
        st.write("Total Hands Raised")
        st.subheader(total_raisehands)

    with othercol:
        st.write("Average Hands Raised")
        st.subheader(average_rasisehands_per_student)
    
    st.markdown("---")



    # ----STUDENTS PERFORMANCE BAR CHART-------
    stdsPerformance_by_nationality = (
        df_selection.groupby(by=["Nationality"]).sum()[["Performance_Index"]].sort_values(by="Performance_Index")

    )
    fig_students_performance = px.bar(
        stdsPerformance_by_nationality,
        x="Performance_Index",
        y=stdsPerformance_by_nationality.index,
        orientation="h",
        title="<b>Students' Performance By Nationallity</b>",
        color_discrete_sequence=["#0083b8"]*len(stdsPerformance_by_nationality),
        template="plotly_white",
    )
    fig_students_performance.update_layout(
        plot_bgcolor="rgb(0,0,0,0)",
        xaxis=(dict(showgrid=False))
    )

    # st.plotly_chart(fig_students_performance)


    #------Students PREVIOUS PERFORMANCE SCORES ---------
    stdsPerformance_by_stageID = (
        df_selection.groupby(by=["StageID"]).sum()[["Previous_Performance_Scores"]].sort_values(by="Previous_Performance_Scores")

        )
    fig_students_performance_previous = px.bar(
            stdsPerformance_by_stageID,
            x="Previous_Performance_Scores",
            y=stdsPerformance_by_stageID.index,
            orientation="v",
            title="<b>Previous Students' Performance Analysis</b>",
            color_discrete_sequence=["#0083b8"]*len(stdsPerformance_by_stageID),
            template="plotly_white",
        )

    fig_students_performance_previous.update_layout(
            plot_bgcolor="rgb(0,0,0,0)",
            yaxis=(dict(showgrid=False)),       
        )

    # st.plotly_chart(fig_students_performance_previous)

    rightcol, leftcol = st.columns(2)
    rightcol.plotly_chart(fig_students_performance, use_container_width=True)
    leftcol.plotly_chart(fig_students_performance_previous, use_container_width=True)

    st.markdown("---")

    # ----PERFORMANCE PIE CHART-------

    pie_chart = px.pie(df_selection,
                       title='Performance Indexes In Different Countries',
                       values='Performance_Index',
                       names='Nationality'
                       )
    st.plotly_chart(pie_chart)

    st.markdown("##")
    st.markdown("---")


    # ------IMAGE AND DATASETS
    st.dataframe(df_selection)
    
    st.markdown("##")
    st.markdown("---")
     
    #  -----PYGWALKER DATA ANALYSIS
    
    # results = pyg.walk(df_selection, dark="light")
    









