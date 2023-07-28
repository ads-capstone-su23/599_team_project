'''Streamlit citation:
https://towardsdatascience.com/how-to-deploy-machine-learning-models-601f8c13ff45
'''

import streamlit as st
import pandas as pd
import numpy as np
import os
import ast  # Import the ast module for literal_eval

# Print current working directory (for debugging)
os.getcwd()

# Print the list of files in the current directory (for debugging)
os.listdir()

# Try to read the file and handle any exceptions
try:
    data01 = pd.read_csv('data_tm_wo_sw_Xy_half1_2023-07-28_10-51-08326790.csv')
    data02 = pd.read_csv('data_tm_wo_sw_Xy_half2_2023-07-28_10-51-08326790.csv')
    data = pd.concat([data01, data02], ignore_index=True)
    y01_arr01 = np.load('data_tm_wo_sw_topic_lst_2023-07-28_10-51-08326790.npy')
    #st.write(data)
except Exception as e:
    st.error(f'CWD: {os.getcwd()}\nList dir: {os.listdir()}\nError: {e}')

#file_in_name01 = 'data_preprocessed_wo_sw_X2_2023-07-25_13-11-04731013.csv'

#data = pd.read_csv(file_in_name01)
#display(data.head())

st.header('Positive News App')
st.text_input('Enter your Name: ', key='name')

if st.checkbox('Show dataframe'):
    data

#topic_lst = ['season draft',
#             'prop runs',
#             'amazon review',
#             'trump president',
#             'business work',
#             'russian prigozhin',
#             'ai generative',
#             'titanic submersible',
#             'inflation rates',
#             'police court']

topic_lst = y01_arr01.tolist()

topic_dict = {}
for idx, t in enumerate(topic_lst):
    topic_dict[t] = idx
    
#print(topic_dict)

st.subheader("Please select Topic(s)!")
left_column, right_column = st.columns(2)
with left_column:
    inp_species = st.multiselect(
        'Topic Name:',
        topic_lst)

if st.button('Find articles rvsd'):
    rev_topic_dict = {v: k for k, v in topic_dict.items()}
    selected_indices = [topic_dict[i] for i in inp_species]
    selected_topic_names = [rev_topic_dict[idx] for idx in selected_indices]
    
    # Convert the 'multilabel' column from string to list of integers
    data['multilabel'] = data['multilabel'].apply(ast.literal_eval)
    
    filtered_data = data[data['multilabel'].apply(lambda x: any(x[topic_dict[name]] == 1 for name in selected_topic_names))]
    fd_display_cols = ['publish_date', 'source_name', 'title', 'url']
    filter_data_d = filtered_data[fd_display_cols]
    st.write(filter_data_d)