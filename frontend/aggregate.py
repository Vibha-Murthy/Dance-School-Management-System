import pandas as pd
import streamlit as st
from database import *

def aggregate():
    result = stud_agg()
    df = pd.DataFrame(result, columns=['School Name', 'Batch ID', 'Number of Students'])
    st.dataframe(df)
