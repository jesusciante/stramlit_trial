import streamlit as st 
import pandas as pd

# DB Mgmt
import sqlite3 
conn = sqlite3.connect('trial.db')
c = conn.cursor()


# Fxn Make Execution
def sql_executor(raw_code):
	c.execute(raw_code)
	data = c.fetchall()
	return data 

st.subheader("HomePage")


st.form(key='Mark Number Search')
raw_code = st.text_area("Mark Number Here")

st.code(raw_code)

query_results = sql_executor("select*from SteelFab where MARKNUMBER like'" + raw_code + "%'")


st.expander("Pretty Table")
query_df = pd.DataFrame(query_results)
st.dataframe(query_df)

