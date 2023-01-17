import pandas as pd
import streamlit as st
from database import *


def delete_performance():
    result = view_all_performance()
    df = pd.DataFrame(result, columns=['Performance ID', 'Venue', 'Date', 'Style', 'Song', 'Costume ID', 'Band ID', 'Trainer ID'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_perf = sorted([i[0] for i in view_only_pid()])
    selected_perf = st.selectbox("Task to Delete", list_of_perf)
    st.warning("Do you want to delete ::{}".format(selected_perf))
    if st.button("Delete Performance"):
        delete_perf(selected_perf)
        st.success("Performance has been deleted successfully")
    new_result = view_all_performance()
    df2 = pd.DataFrame(new_result, columns=['Performance ID', 'Venue', 'Date', 'Style', 'Song', 'Costume ID', 'Band ID', 'Trainer ID'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_musician():
    result = view_all_musician()
    df = pd.DataFrame(result, columns=['Musician ID', 'Name', 'Instrument', 'Band ID'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_musi = sorted([i[0] for i in view_only_muid()])
    selected_musi = st.selectbox("Task to Delete", list_of_musi)
    st.warning("Do you want to delete ::{}".format(selected_musi))
    if st.button("Delete Musician"):
        delete_musi(selected_musi)
        st.success("Musician has been deleted successfully")
    new_result = view_all_musician()
    df2 = pd.DataFrame(new_result, columns=['Musician ID', 'Name', 'Instrument', 'Band ID'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_student():
    result = view_all_student()
    df = pd.DataFrame(result, columns=['Student ID', 'First Name', 'Last Name', 'Join Date', 'Duration', 'DOB', 'Address', 'Batch', 'Performance'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_stud = sorted([i[0] for i in view_only_stdid()])
    selected_stud = st.selectbox("Task to Delete", list_of_stud)
    st.warning("Do you want to delete ::{}".format(selected_stud))
    if st.button("Delete Student"):
        delete_stud(selected_stud)
        st.success("Student has been deleted successfully")
    new_result = view_all_student()
    df2 = pd.DataFrame(new_result, columns=['Student ID', 'First Name', 'Last Name', 'Join Date', 'Duration', 'DOB', 'Address', 'Batch', 'Performance'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_trainer():
    result = view_all_trainer()
    df = pd.DataFrame(result, columns=['T_ID', 'Name', 'Phone_no', 'Style', 'Batch'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_train = sorted([i[0] for i in view_only_tid()])
    selected_train = st.selectbox("Task to Delete", list_of_train)
    st.warning("Do you want to delete ::{}".format(selected_train))
    if st.button("Delete Trainer"):
        delete_train(selected_train)
        st.success("Trainer has been deleted successfully")
    new_result = view_all_trainer()
    df2 = pd.DataFrame(new_result, columns=['T_ID', 'Name', 'Phone_no', 'Style', 'Batch'])
    with st.expander("Updated data"):
        st.dataframe(df2)