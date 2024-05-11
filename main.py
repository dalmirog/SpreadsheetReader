# import spreadsheetreader.SpreadsheetReader as SpreadsheetReader
from spreadsheetreader import Reader
from flask import Flask, jsonify, request
import json
from json import JSONEncoder

# creating a Flask app 
app = Flask(__name__)

reader = Reader(
      spreadsheetId= "1DV-eajMmYxksh1JFdn-LJQ_y8RgdbFBh_-u-vF1hVXA",
      spreadsheetName= "Data",
      columnRange="A2:C")

@app.route('/', methods = ['GET']) 
def home():
    values = reader.execute()
    print(values)
    return 'OK', 200

# driver function 
if __name__ == '__main__':
	
	app.run(debug = True)