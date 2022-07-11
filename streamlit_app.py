# streamlit_app.py
import streamlit as st
from gsheetsdb import connect
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from gspread_pandas import Spread, Client
import pygsheets

#--------INITIALIZATION------------------------
# Create a connection object.
conn = connect()

#Get Sheet URL
sheet_url = st.secrets["public_gsheets_url"]

def query_to_dataframe(_connector, query: str) -> pd.DataFrame:
        rows = _connector.execute(query, headers=1)
        dataframe = pd.DataFrame(list(rows))
        return dataframe

def get_data(_connector, gsheets_url) -> pd.DataFrame:
        return query_to_dataframe(_connector, f'SELECT * FROM "{gsheets_url}"')

#--------HEADER------------------------
st.title('UPD Church Inventory App')
st.header('API made by: Kervee Quinto')
st.markdown(f"## 📝 Connecting to a public Google Sheet")

rows = conn.execute(f'SELECT * FROM "{sheet_url}"', headers=1)
rows = rows.fetchall()


#for row in rows:
#  df = pd.DataFrame(
#    np.random.randn(10, 5),
#   columns=('col %d' % i for i in range(5)))
#  st.table(df)







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
