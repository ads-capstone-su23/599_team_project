'''Streamlit citation:
https://towardsdatascience.com/how-to-deploy-machine-learning-models-601f8c13ff45
'''

import streamlit as st
import pandas as pd
from sklearn.preprocessing import  LabelEncoder
import xgboost as xgb
import numpy as np

'''Dir nav citation:
https://softhints.com/python-change-directory-parent/
'''
curr_dir = os.path.abspath(os.curdir)
print(curr_dir)
os.chdir("..")
up1_dir = os.path.abspath(os.curdir)
print(up1_dir)

# change `data_location` to the location of the folder on your machine.
data_location = 'data'
ref_docs_location = 'ref_docs'

file_in_name01 = 'data_preprocessed_wo_sw_2023-07-20_13-02-01408354.csv'

file_in_path01 = os.path.join(up1_dir, data_location, file_in_name01)

print(f'CSV file in 1 path: {file_in_path01}')

data = pd.read_csv(file_in_path01)
display(data.head())
#data = pd.read_csv("fish.csv")

st.header("Fish Weight Prediction App")
st.text_input("Enter your Name: ", key="name")

if st.checkbox('Show dataframe'):
    data