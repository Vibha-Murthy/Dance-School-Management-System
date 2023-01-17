import pandas as pd
import streamlit as st
from database import *

def proc():
    sy = st.text_input("Costume Re-stocking:")
    if st.button("Re-stock"):
        cost_proc()
        st.success("Costumes:")
        result = view_all_costume()
        df = pd.DataFrame(result, columns=['Costume ID', 'Costume', 'Availability', 'Quantity', 'Store'])
        st.dataframe(df)
    