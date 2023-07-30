'''Streamlit citation:
https://towardsdatascience.com/how-to-deploy-machine-learning-models-601f8c13ff45
Filter citation:
https://chat.openai.com/share/163a4e26-8987-434c-b8c5-20f3749188f8
URL formatting citation:
https://discuss.streamlit.io/t/how-to-display-a-clickable-link-pandas-dataframe/32612/6
'''

import streamlit as st
import pandas as pd
import numpy as np
import os
import random
import ast  # Import the ast module for literal_eval

random_state = 1699
random.seed(random_state)
thresh = .996

article_n = 2
article_nx2 = article_n * 3

# Print current working directory (for debugging)
os.getcwd()

# Print the list of files in the current directory (for debugging)
os.listdir()

# Try to read the file and handle any exceptions
try:
    #data01 = pd.read_csv('data_tm_wo_sw_Xy_half1_2023-07-28_10-51-08326790.csv')
    #data02 = pd.read_csv('data_tm_wo_sw_Xy_half2_2023-07-28_10-51-08326790.csv')
    #data = pd.concat([data01, data02], ignore_index=True)
    data = pd.read_csv('capstone_master_topic_assignment_0729.csv')
    #y01_arr01 = np.load('data_tm_wo_sw_topic_lst_2023-07-28_10-51-08326790.npy')
    #y01_arr01 = np.load('capstone_master_customer_topics.npy')
    # Load pre-processed sentiment
    #data_sa01 = pd.read_csv('data_sa_w_sw_half1_2023-07-28_12-11-33337653.csv')
    #data_sa02 = pd.read_csv('data_sa_w_sw_half2_2023-07-28_12-11-33337653.csv')
    #data_sa = pd.concat([data_sa01, data_sa02],
    #                    ignore_index=True)
    data_sa = pd.read_csv('news-05.csv')
    data = pd.merge(data, data_sa, on='text_id')
    #st.write(data)
except Exception as e:
    st.error(f'CWD: {os.getcwd()}\nList dir: {os.listdir()}\nError: {e}')

st.header('Your Daily Retreat: Positive News App')

if st.checkbox('Show dataframe'):
    data

group_by_cols = ['source_name', 'customer_topics', 'text_id',]

data1a = data.loc[data['sentiment_roberta'] > .8]
data1a = data1a[group_by_cols]
st.write(len(data1a))
st.write(data1a.groupby(by=['source_name', 'customer_topics']).count())

data1b = data.loc[data['sentiment_roberta'] > thresh]
data1b = data1b[group_by_cols]
st.write(len(data1b))
st.write(data1b.groupby(by=['source_name', 'customer_topics']).count())

#topic_lst = y01_arr01.tolist()

#topic_dict = {}
#for idx, t in enumerate(topic_lst):
#    topic_dict[t] = idx
    
#print(topic_dict)

st.subheader("Please select Topic(s) and/or Source(s)!")
left_column, right_column = st.columns(2)
with left_column:
    selected_topics = st.multiselect(
        'Topic Name:',
        data['customer_topics'].unique())

with right_column:
    selected_sources = st.multiselect(
        'Source Name:',
        data['source_name'].unique())

if st.button('Find articles'):
    #rev_topic_dict = {v: k for k, v in topic_dict.items()}
    #selected_indices = [topic_dict[i] for i in selected_topics]
    #selected_topic_names = [rev_topic_dict[idx] for idx in selected_indices]
    #st.write(rev_topic_dict)
    #st.write(selected_topic_names)
    
    # Convert the 'multilabel' column from string to list of integers
    #data['multilabel'] = data['multilabel'].apply(ast.literal_eval)
    
    filtered_data = data.loc[data['sentiment_roberta'] > thresh]
    #filtered_data = filtered_data[filtered_data['multilabel'].apply(lambda x: any(x[topic_dict[name]] == 1 for name in selected_topic_names))]
    topic_len = len(selected_topics)
    #st.write(topic_len)
    source_len = len(selected_sources)
    #st.write(source_len)
    #for t in selected_topics:
    #    st.write(t)
    
    fd_display_cols = ['customer_topics', 'source_name', 'url', 'title', 'publish_date',]
    fd_sort = ['customer_topics', 'source_name', 'publish_date',]

    if topic_len == 0 and source_len == 0:
        filtered_data_s1 = filtered_data.sample(article_nx2,
                                                random_state=random_state)
        
        filtered_data_s1 = filtered_data_s1[fd_display_cols]
        filtered_data_s1 = filtered_data_s1.sort_values(by=fd_sort,
                                                        ascending=False)
        st.write(f'No search criteria entered: {len(filtered_data_s1)} randomly returned')
        #st.write(filtered_data01)

    elif topic_len > 0 and source_len == 0:
        #filtered_data = filtered_data.loc[filtered_data['customer_topics'].isin(selected_topics)]
        filtered_data_s1 = pd.DataFrame()
        for t in selected_topics:
            filtered_data_s2 = filtered_data.loc[filtered_data['customer_topics'] == t]
            try:
                filtered_data_s2 = filtered_data_s2.sample(article_n,
                                                           random_state=random_state)
            except:
                filtered_data_s2 = filtered_data_s2.sample(len(filtered_data_s2),
                                                           random_state=random_state)
            filtered_data_s1 = pd.concat([filtered_data_s1,
                                          filtered_data_s2],
                                         ignore_index=True)
        filtered_data_s1 = filtered_data_s1[fd_display_cols]
        filtered_data_s1 = filtered_data_s1.sort_values(by=fd_sort,
                                                        ascending=False)
        st.write(f"Sample for '{selected_topics}': {len(filtered_data_s1)} randomly returned")
        #st.write(filtered_data02)

    elif topic_len == 0 and source_len > 0:
        #filtered_data = filtered_data.loc[filtered_data['source_name'].isin(selected_sources)]
        filtered_data_s1 = pd.DataFrame()
        for s in selected_sources:
            filtered_data_s2 = filtered_data.loc[filtered_data['source_name'] == s]
            try:
                filtered_data_s2 = filtered_data_s2.sample(article_n,
                                                           random_state=random_state)
            except:
                filtered_data_s2 = filtered_data_s2.sample(len(filtered_data_s2),
                                                           random_state=random_state)
            filtered_data_s1 = pd.concat([filtered_data_s1,
                                          filtered_data_s2],
                                         ignore_index=True)
        filtered_data_s1 = filtered_data_s1[fd_display_cols]
        filtered_data_s1 = filtered_data_s1.sort_values(by=fd_sort,
                                                        ascending=False)
        st.write(f"Sample for '{selected_sources}': {len(filtered_data_s1)} randomly returned")
        #st.write(filtered_data03)

    else:
        #filtered_data = filtered_data.loc[filtered_data['source_name'].isin(selected_sources)]
        #filtered_data = filtered_data.loc[filtered_data['customer_topics'].isin(selected_topics)]
        filtered_data_s1 = pd.DataFrame()
        for s in selected_sources:
            for t in selected_topics:
                filtered_data_s2 = filtered_data.loc[(filtered_data['source_name'] == s) & (filtered_data['customer_topics'] == t)]
                try:
                    filtered_data_s2 = filtered_data_s2.sample(article_n,
                                                               random_state=random_state)
                except:
                    filtered_data_s2 = filtered_data_s2.sample(len(filtered_data_s2),
                                                               random_state=random_state)
                filtered_data_s1 = pd.concat([filtered_data_s1,
                                              filtered_data_s2],
                                             ignore_index=True)
        filtered_data_s1 = filtered_data_s1[fd_display_cols]
        filtered_data_s1 = filtered_data_s1.sort_values(by=fd_sort,
                                                        ascending=False)
        st.write(f"Sample for '{selected_sources}' and '{selected_topics}': {len(filtered_data_s1)} randomly returned")
        #st.write(filtered_data04)
    st.data_editor(
        filtered_data_s1,
        column_config={
            "url": st.column_config.LinkColumn("Article Links",
                                              width='large')
        },
        hide_index=True,)
        
