import datetime

import pandas as pd
import streamlit as st
from database import *


def update_perf():
    result = view_all_performance()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Performance ID', 'Venue', 'Date', 'Style', 'Song', 'Costume ID', 'Band ID', 'Trainer ID'])
    with st.expander("Current Performances"):
        st.dataframe(df)
    list_of_performance = [i[0] for i in view_only_pid()]
    selected_performance = st.selectbox("Performance to Edit", list_of_performance)
    selected_result = get_performance(selected_performance)
    # st.write(selected_result)
    if selected_result:
        pid = selected_result[0][0]
        venue = selected_result[0][1]
        date = selected_result[0][2]
        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_date = st.text_input("Date:", date)
            
        with col2:
            new_venue = st.text_input("Venue:", venue)
        if st.button("Update Performance"):
            edit_perf_data(new_date, new_venue, pid)
            st.success("Successfully updated:: {} to ::{} and {} to ::{}".format(date, new_date, venue, new_venue))

    result2 = view_all_performance()
    df2 = pd.DataFrame(result2, columns=['Performance ID', 'Venue', 'Date', 'Style', 'Song', 'Costume ID', 'Band ID', 'Trainer ID'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_stud():
    result = view_all_student()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Student ID', 'First Name', 'Last Name', 'Join Date', 'Duration', 'DOB', 'Address', 'Batch', 'Performance'])
    with st.expander("Current Students"):
        st.dataframe(df)
    list_of_stud = [i[0] for i in view_only_stdid()]
    selected_stud = st.selectbox("Student to Edit", list_of_stud)
    selected_result = get_stud(selected_stud)
    # st.write(selected_result)
    if selected_result:
        sid = selected_result[0][0]
        dur = selected_result[0][4]
       
        # Layout of Create
        new_dur = st.text_input("Duration:", dur)
        if st.button("Update Student Duration"):
            edit_stud_data(new_dur, sid)
            st.success("Successfully updated:: {} to ::{}".format(dur, new_dur))

    result2 = view_all_student()
    df2 = pd.DataFrame(result2, columns=['Student ID', 'First Name', 'Last Name', 'Join Date', 'Duration', 'DOB', 'Address', 'Batch', 'Performance'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_cost():
    result = view_all_costume()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Costume ID', 'Costume', 'Availability', 'Qty', 'Store'])
    with st.expander("Current Costumes"):
        st.dataframe(df)
    if st.button("Restock Costume"):
        edit_costume_data()
        st.success("Successfully Restock")

    result2 = view_all_costume()
    df2 = pd.DataFrame(result2, columns=['Costume ID', 'Costume', 'Availability', 'Qty', 'Store'])
    with st.expander("Updated data"):
        st.dataframe(df2)
