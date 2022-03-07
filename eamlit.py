import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit


@st.cache
def get_data_from_excel():
    df = pd.read_excel(
        io="SteelFab.xlsx",
        engine="openpyxl",
        sheet_name="Sheet1",
        header=0,
    )
    # Add 'hour' column to dataframe
    return df

st.title('RHI - A1 Package - Updated Marks Data Visualiation ')

st.markdown("""
This application has been prepared to observe the current mark and KMD statuses with the data in the database.
 """)

st.sidebar.header('User Input Features')
selected_mark = st.sidebar.text_input("Mark Number for Search")

#"P.2P1.DA-124/1"

df = get_data_from_excel()

df2 = df[df['MARK NUMBER']] == selected_mark

st.markdown(st.write(df2))