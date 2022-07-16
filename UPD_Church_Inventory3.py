from lib2to3.pgen2.token import NAME
from turtle import pd

#---Connect to Streamlit--------------
import streamlit as st
st.set_page_config(page_title='UPD Church Inventory API',layout='wide')

#---Connect to Google Sheet--------
from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
import gspread_pandas as gpd
import gspread
import numpy as np

#---Header Section-----------------
st.header("UPD Church Inventory API")
st.text("An API made by Kervee Quinto")
barcode = st.text_input("Input a valid barcode")
if not barcode:
    #outputs error for null entries
    st.error('No barcode with this value is stored in the Google sheet')
if barcode:
    try:
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

        worksheet = sh.worksheet('all_box')
        list_of_lists = worksheet.get_all_values()
        filtered_list = []

        if barcode == "1320793936":
            for i in list_of_lists:
                if i[2] == "1":
                    filtered_list.append(i)


        elif barcode == "1320793931":
            for i in list_of_lists:
                if i[2] == "2":
                    filtered_list.append(i)

        elif barcode == "1989666069":
            for i in list_of_lists:
                if i[2] == "3":
                    filtered_list.append(i)

        df = pd.DataFrame(filtered_list)
        df.columns = ["Name", "Quantity", "Box No."]

        st.dataframe(df)
    
    except:
        st.error("No barcode with this value is stored in the Google sheet")
