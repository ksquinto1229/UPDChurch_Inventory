# streamlit_app.py
import streamlit as st
from gsheetsdb import connect
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from gspread_pandas import Spread, Client

#--------INITIALIZATION------------------------
# Create a connection object.
conn = connect()

#Get Sheet URL
sheet_url = st.secrets["public_gsheets_url"]

#--------HEADER------------------------
st.title('UPD Church Inventory App')
st.header('API made by: Kervee Quinto')


url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

stocks_df = pd.read_html(url, header=0)[0]

stocks_df.head()






# Perform SQL query on the Google Sheet.
#@st.cache(ttl=600)
#def run_query(query):
#    rows = conn.execute(query, headers=1)
#    rows = rows.fetchall()
#    return rows

#rows = run_query(f'SELECT * FROM "{sheet_url}"')

### Print results.
#for row in rows:
#    st.write(f"{row.name} has a :{row.pet}:")
#st.write(sheet_url)
