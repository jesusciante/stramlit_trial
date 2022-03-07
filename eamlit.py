import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit


df = pd.read_excel("SteelFab.xlsx", header=0,sheet_name="Sheet1")

st.title('RHI - A1 Package - Updated Marks Data Visualiation ')

st.markdown("""
This application has been prepared to observe the current mark and KMD statuses with the data in the database.
 """)

st.sidebar.header('User Input Features')
selected_mark = st.sidebar.text_input("Mark Number for Search")


df2 = df[df['MARK NUMBER'] == selected_mark]

#"P.2P1.DA-124/1"

st.markdown(st.write(df2))