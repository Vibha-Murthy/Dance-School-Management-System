import streamlit as st
from database import *
import pandas as pd

def run_query():
     q = st.text_input("Your query:")
     if st.button("Run query"):
        d = query(q)
        st.success("Query has been executed successfully")
        df = pd.DataFrame(d)
        st.dataframe(df)