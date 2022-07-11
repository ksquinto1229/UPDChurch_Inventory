# streamlit_app.py
import pandas as pd
import requests
import streamlit as st
from gsheetsdb import connect

# Create a connection object.
conn = connect()

st.title('UPD ChurchInventory App')
st.header('API made by: Kervee Quinto')


# Perform SQL query on the Google Sheet.
#@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

#sheet_url = st.secrets["public_gsheets_url"]
#rows = run_query(f'SELECT * FROM "{sheet_url}"')

### Print results.
#for row in rows:
#    st.write(f"{row.name} has a :{row.pet}:")

result = conn.execute("""
    SELECT
        country
      , SUM(cnt)
    FROM
        "https://docs.google.com/spreadsheets/d/1_rN3lm0R_bU3NemO0s9pbFkY5LQPcuy1pscv8ZXPtg8/"
    GROUP BY
        country
""", headers=1)
for row in result:
    print(row)
