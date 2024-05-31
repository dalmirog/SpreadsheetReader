from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from .authentication import getCreds

class Reader:
    def __init__(self, spreadsheetId, spreadsheetName):
        self.spreadsheetId = spreadsheetId
        self.spreadsheetName = spreadsheetName
        self.columnRange = "A:Z"

    def execute(self):

        """Shows basic usage of the Sheets API.
        Prints values from a sample spreadsheet.
        """
        # The ID and range of a sample spreadsheet.
        SAMPLE_SPREADSHEET_ID = self.spreadsheetId
        SAMPLE_RANGE_NAME = f"{self.spreadsheetName}!{self.columnRange}" # TODO Remove column range option and instead go with A:Z.
        # TODO Create a class that dinamically creates json objects based on A1 as header names and then the rest as data

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
            return values[1:]
        except HttpError as err:
            print(err)