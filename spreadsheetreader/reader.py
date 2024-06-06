from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from .authentication import get_creds

class Reader:
    def __init__(self, spreadsheet_id, spreadsheet_name):
        self.spreadsheet_id = spreadsheet_id
        self.spreadsheet_name = spreadsheet_name
        self.column_range = "A:Z"

    def execute(self):
        creds = get_creds()

        try:
            service = build("sheets", "v4", credentials=creds)
            sheet = service.spreadsheets()
            result = (
                sheet.values()
                .get(spreadsheetId=self.spreadsheet_id, range=f"{self.spreadsheet_name}!{self.column_range}")
                .execute()
            )
            values = result.get("values", [])

            if not values:
                print("No data found.")
                return
            return values
        except HttpError as err:
            print(err)