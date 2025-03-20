import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

# st.title("dv")
st.set_page_config(page_title="dv",
	page_icon="🤣")
st.title("data visualization with streamit")
with st.sidebar:
	uplode=st.file_uploader("uplodde csv")
if uplode is not None:
	df=pd.read_csv(uplode)
	st.dataframe(df.head())