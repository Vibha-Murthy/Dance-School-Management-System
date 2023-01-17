import streamlit as st
from database import *


def create_musician():
    col1, col2 = st.columns(2)
    with col1:
        musician_id = st.number_input("ID:", min_value=9000, max_value=9100, step=1)
        musician_name = st.text_input("Name:")
    with col2:
        musician_instr = st.text_input("Instrument: ")
        musician_band_id = st.number_input("Band ID:", min_value=6000, max_value=6100, step=1)
    if st.button("Add Musician"):
        add_data_musician(musician_id, musician_name, musician_instr, musician_band_id)
        st.success("Successfully added Musician: {}".format(musician_name))

def create_band():
    col1, col2 = st.columns(2)
    with col1:
        band_id = st.number_input("ID:", min_value=6000, max_value=6100, step=1)
    with col2:
        band_name = st.text_input("Name:")
    if st.button("Add Band"):
        add_data_band(band_id, band_name)
        st.success("Successfully added Band: {}".format(band_name))

def create_costume():
    col1, col2 = st.columns(2)
    with col1:
        c_ID = st.number_input("Costume ID:", min_value=7000, max_value=7100, step=1)
        costume = st.text_input("Costume:")
    with col2:
        avail = st.text_input("Availability (Y/N): ")
        qty = st.number_input("Quantity:", min_value=0, max_value=100, step=1)
        store = st.text_input("Store: ")
    if st.button("Add Costume"):
        add_data_costume(c_ID, costume, avail, qty, store)
        st.success("Successfully added Costume: {}".format(costume))

def create_style():
    col1, col2 = st.columns(2)
    with col1:
        d_ID = st.number_input("Style ID:", min_value=5000, max_value=5100, step=1)
    with col2:
        style = st.text_input("Style: ")

    if st.button("Add Style"):
        add_data_dancestyle(d_ID, style)
        st.success("Successfully added Dance Style : {}".format(style))

def create_school():
    col1, col2 = st.columns(2)
    with col1:
        s_ID = st.number_input("School ID:", min_value=1, max_value=100, step=1)
        schname = st.text_input("Name:")
    with col2:
        srtdt = st.text_input("Start Date (YYYY-MM-DD): ")
        loc = st.text_input("Location : ")
    if st.button("Add School"):
        add_data_danceschool(s_ID, schname, srtdt, loc)
        st.success("Successfully added School: {}".format(schname))

def create_batch():
    col1, col2 = st.columns(2)
    with col1:
        b_ID = st.number_input("Batch ID:", min_value=800, max_value=900, step=1)
        hw = st.text_input("Homework:")
    with col2:
        s_ID = st.number_input("School ID:", min_value=0, max_value=100, step=1)
    if st.button("Add Batch"):
        add_data_batch(b_ID, hw, s_ID)
        st.success("Successfully added Batch: {}".format(b_ID))

def create_trainer():
    col1, col2 = st.columns(2)
    with col1:
        t_ID = st.number_input("Trainer ID:", min_value=2000, max_value=2100, step=1)
        trnname = st.text_input("Name:")
        phn = st.number_input("Phone No:", min_value=1000000000, max_value=9999999999, step=1)
    with col2:
        d_ID = st.number_input("Trainer Dance Style:", min_value=5000, max_value=5100, step=1)
        b_ID = st.number_input("Batch ID:", min_value=800, max_value=900, step=1)
    if st.button("Add Trainer"):
        add_data_trainer(t_ID, trnname, phn, d_ID, b_ID)
        st.success("Successfully added Trainer: {}".format(trnname))

def create_student():
    col1, col2 = st.columns(2)
    with col1:
        std_ID = st.number_input("Student ID:", min_value=1, max_value=800, step=1)
        f_name = st.text_input("First Name:")
        l_name = st.text_input("Last Name:")
        jndt = st.text_input("Join Date (YYYY-MM-DD): ")
        dob = st.text_input(" DOB (YYYY-MM-DD): ")
    with col2:
        dur = st.number_input("Duration:", min_value=1, max_value=100, step=1)
        addr = st.text_input("Address:")
        b_ID = st.number_input("Batch ID:", min_value=800, max_value=900, step=1)
        p_ID = st.number_input("Performance ID (if any):", min_value=4000, max_value=4100, step=1)
    if st.button("Add Student"):
        add_data_student(std_ID, f_name, l_name, jndt, dur, dob, addr, b_ID, p_ID)
        st.success("Successfully added Student: {}".format(f_name))

def create_performance():
    col1, col2 = st.columns(2)
    with col1:
        p_ID = st.number_input("Performance ID:", min_value=4000, max_value=4100, step=1)
        venue = st.text_input("Venue:")
        date = st.text_input(" Date (YYYY-MM-DD): ")
        c_ID = st.number_input("Costume ID:", min_value=7000, max_value=7100, step=1)
    with col2:
        style = st.number_input("Dance Style:", min_value=5000, max_value=5100, step=1)
        song = st.text_input("Song:")
        m_ID = st.number_input("Performance ID:", min_value=6000, max_value=6100, step=1)
        t_ID = st.number_input("Trainer ID:", min_value=2000, max_value=2100, step=1)
    if st.button("Add Performance"):
        add_data_performance(p_ID,venue,date,style,song,c_ID,m_ID,t_ID)
        st.success("Successfully added Performance: {}".format(p_ID))