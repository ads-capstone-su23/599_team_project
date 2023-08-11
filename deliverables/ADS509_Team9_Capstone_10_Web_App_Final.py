# Daily Retreat: Using Sentiment Analysis to Find, Personalize,
# and Share Positive News from Popular Online Sources
# Aaron Carr, Azucena Faus, and Dave Friesen - ADS-599-01-SU23

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

# Set random state; can be eliminated for production to create psuedo-random samples
random_state = 1699
random.seed(random_state)
thresh = .9984

# Set global sample return n
article_n = 2
article_nx2 = article_n * 3

# Print current working directory (for debugging)
os.getcwd()

# Print the list of files in the current directory (for debugging)
os.listdir()

# Try to read the file and handle any exceptions
try:
    data = pd.read_csv('capstone_master_topic_assignment_0729.csv')
    data_sa = pd.read_csv('news-05.csv')
    data = pd.merge(data, data_sa, on='text_id')
    #st.write(data)
except Exception as e:
    st.error(f'CWD: {os.getcwd()}\nList dir: {os.listdir()}\nError: {e}')

# Set page header
st.header('Your Daily Retreat: Positive News App')

# Option to show raw dataframe
if st.checkbox('Show dataframe'):
    data

# Set col selection for aggregate df's
group_by_cols = ['source_name', 'customer_topics', 'text_id',]

# Compare summaries by different thresholds
data1a = data.loc[data['sentiment_roberta'] > .8]
data1a = data1a[group_by_cols]
#st.write(len(data1a))
#st.write(data1a.groupby(by=['source_name', 'customer_topics']).count())
data1b = data.loc[data['sentiment_roberta'] > thresh]
data1b = data1b[group_by_cols]
#st.write(len(data1b))
#st.write(data1b.groupby(by=['source_name', 'customer_topics']).count())

st.subheader("Please select Topic(s) and/or Source(s)! Or just hit 'Find Articles' for a random selection")

# Display query filters
left_column, right_column = st.columns(2)
with left_column:
    selected_topics = st.multiselect(
        'Topic Name:',
        data['customer_topics'].unique())

with right_column:
    selected_sources = st.multiselect(
        'Source Name:',
        data['source_name'].unique())

# Run query to find sample articles based on user-specified filters
if st.button('Find Articles'):
    filtered_data = data.loc[data['sentiment_roberta'] > thresh]
    topic_len = len(selected_topics)
    #st.write(topic_len)
    source_len = len(selected_sources)
    #st.write(source_len)
    #for t in selected_topics:
    #    st.write(t)
    
    # Col selection for display & sort
    fd_display_cols = ['customer_topics', 'source_name', 'url', 'title', 'publish_date',]
    fd_sort = ['customer_topics', 'source_name', 'publish_date',]
    
    # Condition 1: No sources or topics selected
    if topic_len == 0 and source_len == 0:
        filtered_data_s1 = filtered_data.sample(article_nx2,
                                                random_state=random_state)
        
        filtered_data_s1 = filtered_data_s1[fd_display_cols]
        filtered_data_s1 = filtered_data_s1.sort_values(by=fd_sort,
                                                        ascending=False)
        st.write(f'No search criteria entered: {len(filtered_data_s1)} randomly returned')
        #st.write(filtered_data01)

    # Condition 2: No sources selected
    elif topic_len > 0 and source_len == 0:
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

    # Condition 3: No topics selected
    elif topic_len == 0 and source_len > 0:
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

    # Condition 4: Sources and topics selected
    else:
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
        
    # Use streamlit method to format resulting dataframe
    st.data_editor(
        filtered_data_s1,
        column_config={
            'url': st.column_config.LinkColumn('Article Link',
                                               width='large'),
            'customer_topics': st.column_config.TextColumn('Topic',
                                                           width='medium'),
            'source_name': st.column_config.TextColumn('Source',
                                                       width='medium'),
            'title': st.column_config.TextColumn('Article Title',
                                                 width='large'),
            'publish_date': st.column_config.TextColumn('Publish Date',
                                                        width='medium'),
        },
        hide_index=True,)
        
