'''Streamlit citation:
https://towardsdatascience.com/how-to-deploy-machine-learning-models-601f8c13ff45
'''

import streamlit as st
import pandas as pd
import numpy as np
import os

# Print current working directory (for debugging)
print(os.getcwd())

# Print the list of files in the current directory (for debugging)
print(os.listdir())

# Try to read the file and handle any exceptions
try:
    data = pd.read_csv("data_preprocessed_wo_sw_X2_2023-07-25_13-11-04731013.csv")
    st.write(data)
except Exception as e:
    st.error(f"Error: {e}")

#file_in_name01 = 'data_preprocessed_wo_sw_X2_2023-07-25_13-11-04731013.csv'

#data = pd.read_csv(file_in_name01)
#display(data.head())

st.header("Fish Weight Prediction App")
st.text_input("Enter your Name: ", key="name")

if st.checkbox('Show dataframe'):
    data