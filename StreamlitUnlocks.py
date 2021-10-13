import pandas as pd
import streamlit as st

df1 = pd.read_csv(r'C:\Users\L.SCHEUER\PycharmProjects\VSO-Token-Unlocks\VSO Unlocks Not Ordered.csv')
df2 = pd.read_csv(r'C:\Users\L.SCHEUER\PycharmProjects\VSO-Token-Unlocks\VSO Unlocks Grouped by Days Until Unlock.csv')

st.write(
    """
    # VSO Unlocks Dashboard
    """
)
st.subheader('VSO unlock amount by days until unlock')
st.bar_chart(df2['VSO Amount'])

st.subheader('Cummulative VSO unlocks')
st.bar_chart(df2['Cummulative VSO Unlocks'])