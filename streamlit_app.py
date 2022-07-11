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

gc = pygsheets.authorize(service_file='/Users/user/desktop/melodic-bearing-356014-bf79a26ed93c.json')
sh = gc.open('UPDChurch_Inventory_Spreadsheet')


df = pd.DataFrame()
df['name'] = ['John', 'Steve', 'Sarah']

#--------HEADER------------------------
st.title('UPD Church Inventory App')
st.header('API made by: Kervee Quinto')

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
