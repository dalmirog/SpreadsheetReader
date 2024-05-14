from api import app, result_parser, message
from spreadsheetreader import Reader
from flask import jsonify

reader = Reader(
      spreadsheetId = app.config['SPREADSHEETID'],
      spreadsheetName = app.config['SPREADSHEETNAME'],
      columnRange = app.config['COLUMNRANGE'])

@app.route('/', methods = ['GET']) 
def home():
      rawValues = reader.execute()
      messages = [message.Message(rv[0], rv[1], rv[2]) for rv in rawValues]
      messages_dict = [message.to_dict() for message in messages]
      return jsonify(messages_dict), 200