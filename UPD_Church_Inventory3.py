from lib2to3.pgen2.token import NAME
import streamlit as st

#---Connect to Google Sheet--------
from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
import gspread_pandas as gpd
import gspread
import numpy as np

#---Connect to Streamlit--------------
st.set_page_config(page_title='UPD Church Inventory API',layout='wide')

#---Header Section-----------------
st.header("UPD Church Inventory API")
st.text("An API made by Kervee Quinto")
barcode = st.text_input("Input a valid barcode")
        
if not barcode:
    #outputs error for null entries
    st.error('No barcode with this value is stored in the Google sheet')
if barcode:
    try:
        query:
        #initialize scope
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',
        "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        service_account_file = "melodic-bearing-356014-bf79a26ed93c.json"

        creds = None
        creds = service_account.Credentials.from_service_account_file(
            service_account_file, scopes=scope
        )

        SAMPLE_SPREADSHEET_ID = '1igr3ftdUzFDUO6SnbjpLLIxiEPHZS19mCBgItU2Hzl4'

        service = build('sheets', 'v4', credentials=creds)

        #Call the Sheets API
        sheet = service.spreadsheets()

        gc = gspread.service_account(filename='melodic-bearing-356014-bf79a26ed93c.json')     
        sh = gc.open_by_key('1igr3ftdUzFDUO6SnbjpLLIxiEPHZS19mCBgItU2Hzl4')

        worksheet = sh.worksheet(barcode)
        list_of_lists = worksheet.get_all_values()
        df = pd.DataFrame(list_of_lists)

        st.dataframe(df)
        
        if st.button('Refresh Table'):
            goto query
        else:
            st.error("No Table Yet")
    
    except:
        st.error("No barcode with this value is stored in the Google sheet")








