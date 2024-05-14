import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class Reader:
    def __init__(self, spreadsheetId, spreadsheetName, columnRange):
        self.spreadsheetId = spreadsheetId
        self.spreadsheetName = spreadsheetName
        self.columnRange = columnRange

    def execute(self):
        # If modifying these scopes, delete the file token.json.
        SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

        """Shows basic usage of the Sheets API.
        Prints values from a sample spreadsheet.
        """
        # The ID and range of a sample spreadsheet.
        SAMPLE_SPREADSHEET_ID = self.spreadsheetId
        SAMPLE_RANGE_NAME = f"{self.spreadsheetName}!{self.columnRange}"

        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists("token.json"): # TODO make this external to the container so it can be used from anywhere
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", SCOPES
                )
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())

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

            print("Timestamp, Handle, Message:")
            # for row in values:
            #     # Print columns A and E, which correspond to indices 0 and 4.
            #     print(f"{row[0]}, {row[1]}, {row[2]}")
            return values
        except HttpError as err:
            print(err)