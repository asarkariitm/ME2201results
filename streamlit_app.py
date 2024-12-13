import pandas as pd
import streamlit as st

allbatches = pd.read_csv("allbatches.csv")
roll = st.text_input("Enter Roll Number - Alphabets in Capital")

out = allbatches.loc[allbatches['RollNo'].str.contains(roll)]

if st.button('Check Results'):
    st.write(out)
else:
    st.write('Wait for Results')
