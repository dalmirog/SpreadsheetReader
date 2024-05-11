from api import app
from spreadsheetreader import Reader

reader = Reader(
      spreadsheetId = app.config['SPREADSHEETID'],
      spreadsheetName = app.config['SPREADSHEETNAME'],
      columnRange = app.config['COLUMNRANGE'])

@app.route('/', methods = ['GET']) 
def home():
    values = reader.execute()
    print(values)
    return 'OK', 200