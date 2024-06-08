from flask import jsonify, request
from api import app
from spreadsheetreader import Reader
from .utils import create_messages_from_raw_values

@app.route('/messages', methods=['GET'])
def home():
    # Extracting values from the query string
    spreadsheet_id = request.args.get('spreadsheet_id')
    spreadsheet_name = request.args.get('spreadsheet_name')

    # Ensure spreadsheet_id and spreadsheet_name are provided
    if not spreadsheet_id or not spreadsheet_name:
        return jsonify({"error": "spreadsheet_id and spreadsheet_name are required"}), 400

    reader = Reader(
        spreadsheet_id=spreadsheet_id,
        spreadsheet_name=spreadsheet_name
    )

    raw_values = reader.execute()
    messages = create_messages_from_raw_values(raw_values)

    return jsonify(messages), 200

if __name__ == '__main__':
    app.run(debug=True)
