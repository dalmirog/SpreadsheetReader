# SpreadsheetReader

Welcome to SpreadsheetReader! This repository contains code for a spreadsheet reader tool.

## Prerequisites

Before you begin, ensure you have the following:

- A Google account
- Python installed on your machine
- `pip` (Python package installer) installed
- A Google project created following the instructions from the [Google Workspace Guide](https://developers.google.com/workspace/guides/create-project)
- Have the spreadsheet you want to read already created in Google Sheets

## Getting Started

Follow these steps to get started with SpreadsheetReader:

1. Run the following command in your terminal to download the code:
    ```bash
    curl -LJO https://github.com/dalmirog/SpreadsheetReader/archive/master.zip
    ```

2. Unzip the downloaded `master.zip` file.

3. Set up your environment in Google following the instructions [here](https://developers.google.com/sheets/api/quickstart/python#set_up_your_environment) until you download the `credentials.json` file into the `SpreadsheetReader-master` folder.

4. Fill the content of `config.json` inside the `SpreadsheetReader-master` folder with the ID of the spreadsheet and the name of the tab:
    ```json
    {
        "SPREADSHEETID" : "your_spreadsheet_id",
        "SPREADSHEETNAME" : "your_data_tab_name"
    }
    ```

5. Navigate to the unzipped directory and run the `run.py` file:
    ```bash
    cd SpreadsheetReader-master
    python run.py
    ```

## License

This project is licensed under the [MIT License](LICENSE).