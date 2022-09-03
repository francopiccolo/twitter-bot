import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

def get_client(creds_file):
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file)
    return gspread.authorize(creds)

def get_data(client, spreadsheet, sheet):
    sheet = client.open(spreadsheet).worksheet(sheet)
    return sheet.get_all_records()

def append_row(sheet, row):
    sheet.values_append(row)