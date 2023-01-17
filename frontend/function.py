import pandas as pd
import streamlit as st
from database import *

def func():
    sy = st.number_input("Style:", min_value=5000)
    if st.button("Get Trainers"):
        cnt = style_func(sy)
        st.success("Number of trainers:")
        df = pd.DataFrame(cnt, columns=['Style', 'Count', 'Batch ID'])
        st.dataframe(df)
    