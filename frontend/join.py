import pandas as pd
import streamlit as st
from database import *

def join():
    result = perf_join()
    df = pd.DataFrame(result, columns=['PID', 'Venue', 'Date', 'Style', 'Song', 'Band', 'Costume','Costume Availability', 'Choreographer', 'No. of Performers' ])
    st.dataframe(df)