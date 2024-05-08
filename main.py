import SpreadsheetReader

def main():
  SpreadsheetReader.read(
    spreadsheetId= "1DV-eajMmYxksh1JFdn-LJQ_y8RgdbFBh_-u-vF1hVXA",
    spreadsheetName= "Data",
    columnRange="A2:C"
  )

if __name__ == "__main__":
  main()