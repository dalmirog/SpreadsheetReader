from api import app, result_formatter
from spreadsheetreader import Reader
from flask import jsonify, request
from .utils import create_messages_from_raw_values

@app.route('/messages', methods=['GET'])
def home():
    single_line = request.args.get('singleLine', default='false').lower() == 'true'
    
    reader = Reader(
        spreadsheetId=app.config['SPREADSHEETID'],
        spreadsheetName=app.config['SPREADSHEETNAME'],
        columnRange=app.config['COLUMNRANGE']
    )  # TODO Reader should be created using dependency injection

    rawValues = reader.execute()
    messages = create_messages_from_raw_values(rawValues)

    if single_line:
        single_line_messages = result_formatter.single_line(messages)
        return jsonify(single_line_messages), 200

    
    messages_dict = result_formatter.to_dict(messages)
    return jsonify(messages_dict), 200
