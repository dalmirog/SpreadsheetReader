import os

class Config:
    SPREADSHEETID = os.environ.get('SPREADSHEETID')
    SPREADSHEETNAME = os.environ.get('SPREADSHEETNAME')
    COLUMNRANGE = os.environ.get('COLUMNRANGE')


