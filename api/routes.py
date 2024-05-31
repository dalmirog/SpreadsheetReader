from flask import jsonify, request
from api import app, result_formatter
from spreadsheetreader import Reader
from .utils import create_messages_from_raw_values

@app.route('/messages', methods=['GET'])
def home():
    split_results = request.args.get('splitresults', default='false').lower() == 'true'
    
    reader = Reader(
        spreadsheetId=app.config['SPREADSHEETID'],
        spreadsheetName=app.config['SPREADSHEETNAME']
    )  # TODO Reader should be created using dependency injection

    raw_values = reader.execute()
    messages = create_messages_from_raw_values(raw_values)

    if split_results:
        messages_dict = result_formatter.to_dict(messages)
        return jsonify(messages_dict), 200
    single_line_messages = result_formatter.single_line(messages)
    return jsonify(single_line_messages), 200
