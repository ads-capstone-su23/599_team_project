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
    #st.write(data)
except Exception as e:
    st.error(f"CWD: {os.getcwd()}\nList dir: {os.listdir()}\nError: {e}")

#file_in_name01 = 'data_preprocessed_wo_sw_X2_2023-07-25_13-11-04731013.csv'

#data = pd.read_csv(file_in_name01)
#display(data.head())

st.header("Positive News App")
st.text_input("Enter your Name: ", key="name")

if st.checkbox('Show dataframe'):
    data.head()

topic_lst = ['season draft',
         'prop runs',
         'amazon review',
         'trump president',
         'business work',
         'russian prigozhin',
         'ai generative',
         'titanic submersible',
         'inflation rates',
         'police court']

topic_dict = {}
for idx, t in enumerate(topic_lst):
    topic_dict[idx] = t
    
#print(topic_dict)

st.subheader("Please select Topic(s)!")
left_column, right_column = st.columns(2)
with left_column:
    inp_species = st.selectbox(
        'Topic Name:',
        topic_lst)