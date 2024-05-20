from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from .authentication import getCreds

class Reader:
    def __init__(self, spreadsheetId, spreadsheetName, columnRange):
        self.spreadsheetId = spreadsheetId
        self.spreadsheetName = spreadsheetName
        self.columnRange = columnRange

    def execute(self):
        
        """Shows basic usage of the Sheets API.
        Prints values from a sample spreadsheet.
        """
        # The ID and range of a sample spreadsheet.
        SAMPLE_SPREADSHEET_ID = self.spreadsheetId
        SAMPLE_RANGE_NAME = f"{self.spreadsheetName}!{self.columnRange}"

        creds = getCreds()

        try:
            service = build("sheets", "v4", credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = (
                sheet.values()
                .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
                .execute()
            )
            values = result.get("values", [])

            if not values:
                print("No data found.")
                return
            return values
        except HttpError as err:
            print(err)