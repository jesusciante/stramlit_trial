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




def main():
	st.title("SQLPlayground")


st.subheader("HomePage")


st.form(key='query_form')
raw_code = st.text_area("SQL Code Here")


st.code(raw_code)

query_results = sql_executor(raw_code)


st.expander("Pretty Table")
query_df = pd.DataFrame(query_results)
st.dataframe(query_df)





if __name__ == '__main__':
	main()
