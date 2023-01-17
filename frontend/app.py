# Importing pakages
import streamlit as st
from create import *
from database import *
from delete import *
from read import *
from update import *
from query import *
from aggregate import *
from join import *
from function import *

def main():
    st.title("Dance School System PES1UG20CS495")
    menu = ["Add", "View", "Edit", "Remove", "Student Count", "Performance Details (Join)", "Function", "Your Query"]
    mn =  ["Musician", "Music Band", "Costume", "Dance Style", "Dance School", "Batch", "Trainer", "Student", "Performance"]
    del_mn =  ["Musician", "Trainer", "Student", "Performance"]
    up_mn =  ["Costume", "Student", "Performance"]
    choice = st.sidebar.selectbox("Menu", menu)
    #st.image("https://media.4-paws.org/1/e/d/6/1ed6da75afe37d82757142dc7c6633a532f53a7d/VIER%20PFOTEN_2019-03-15_001-2886x1999-1920x1330.jpg")

    #create_table()
    if choice == "Add":
        st.subheader("Choose which table you want to add to :")
        ch = st.selectbox("Tables: ", mn)
        if ch == "Musician":
            create_musician()
        elif ch == "Music Band":
            create_band()
        elif ch == "Costume":
            create_costume()
        elif ch == "Dance Style":
            create_style()
        elif ch == "Dance School":
            create_school()
        elif ch == "Batch":
            create_batch()
        elif ch == "Trainer":
            create_trainer()
        elif ch == "Student":
            create_student()
        elif ch == "Performance":
            create_performance()
    
    elif choice == "Your Query":
        run_query()

    elif choice == "View":
        st.subheader("View all performances")
        read()

    elif choice == "Edit":
        st.subheader("Update created tasks")
        ch1 = st.selectbox("Tables: ", up_mn)
        if ch1 == "Costume":
            update_cost()
        elif ch1 == "Student":
            update_stud()
        elif ch1 == "Performance":
            update_perf()

    elif choice == "Remove":
        ch2 = st.selectbox("Tables: ", del_mn)
        if ch2 == "Musician":
            delete_musician()
        elif ch2 == "Trainer":
            delete_trainer()
        elif ch2 == "Student":
            delete_student()
        elif ch2 == "Performance":
            delete_performance()

    elif choice == "Student Count":
        st.subheader("Count of students in a batch")
        aggregate()

    elif choice == "Performance Details (Join)":
        st.subheader("All details of a performance")
        join()
    
    elif choice == "Function":
        st.subheader("Input the dance style to see how many trainers are available for that style")
        func()

    

    else:
        st.subheader("About tasks")

if __name__ == '__main__':
    main()
