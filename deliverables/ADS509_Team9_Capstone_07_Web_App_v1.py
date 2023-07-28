'''Streamlit citation:
https://towardsdatascience.com/how-to-deploy-machine-learning-models-601f8c13ff45
Filter citation:
https://chat.openai.com/share/163a4e26-8987-434c-b8c5-20f3749188f8
'''

import streamlit as st
import pandas as pd
import numpy as np
import os
import random
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
    # Load pre-processed sentiment
    data_sa01 = pd.read_csv('data_sa_w_sw_half1_2023-07-28_12-11-33337653.csv')
    data_sa02 = pd.read_csv('data_sa_w_sw_half2_2023-07-28_12-11-33337653.csv')
    data_sa = pd.concat([data_sa01, data_sa02], ignore_index=True)
    data = pd.merge(data, data_sa, on='text_id')
    #st.write(data)
except Exception as e:
    st.error(f'CWD: {os.getcwd()}\nList dir: {os.listdir()}\nError: {e}')

#file_in_name01 = 'data_preprocessed_wo_sw_X2_2023-07-25_13-11-04731013.csv'

#data = pd.read_csv(file_in_name01)
#display(data.head())

st.header('Your Daily Retreat: Positive News App')
#st.text_input('Enter your Name: ', key='name')

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

random_state = 1699
random.seed(random_state)

if st.button('Find articles'):
    rev_topic_dict = {v: k for k, v in topic_dict.items()}
    selected_indices = [topic_dict[i] for i in inp_species]
    selected_topic_names = [rev_topic_dict[idx] for idx in selected_indices]
    
    # Convert the 'multilabel' column from string to list of integers
    data['multilabel'] = data['multilabel'].apply(ast.literal_eval)
    
    data_hlink = data.copy()
    #data_hlink['url'] = data_hlink['url'].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')
    #data_hlink['url'] = data_hlink['url'].apply(to_html, escape=False)
    #st.write(data_with_hyperlinks, unsafe_allow_html=True)
    #data_hlink = data_hlink.to_html(escape=False)

    filtered_data = data_hlink.loc[data_hlink['sentiment_bert'] > .9]
    #for t in selected_topic_names:
    filtered_data = filtered_data[filtered_data['multilabel'].apply(lambda x: any(x[topic_dict[name]]==1 for name in selected_topic_names))]
    fd_display_cols = ['publish_date', 'source_name', 'title', 'url']
    filtered_data = filtered_data[fd_display_cols]
    filtered_data = filtered_data.sample(5, random_state=random_state)
    filtered_data = filtered_data.sort_values(by=['publish_date', 'source_name'], ascending=False)
    st.write(filtered_data, unsafe_allow_html=True)