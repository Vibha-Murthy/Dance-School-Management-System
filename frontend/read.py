import pandas as pd
import streamlit as st
import plotly.express as px
from database import *


def read():
    result = view_all_performance()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Performance ID', 'Venue', 'Date', 'Style', 'Song', 'Costume ID', 'Band ID', 'Trainer ID'])
    with st.expander("View all Performances"):
        st.dataframe(df)
    with st.expander("Performance Location"):
        task_df = df['Venue'].value_counts().to_frame()
        task_df = task_df.reset_index()
        st.dataframe(task_df)
        p1 = px.pie(task_df, names='index', values='Venue')
        st.plotly_chart(p1)