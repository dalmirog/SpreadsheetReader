# import spreadsheetreader.SpreadsheetReader as SpreadsheetReader
from spreadsheetreader import reader
def main():
  reader.execute(
    spreadsheetId= "1DV-eajMmYxksh1JFdn-LJQ_y8RgdbFBh_-u-vF1hVXA",
    spreadsheetName= "Data",
    columnRange="A2:C"
  )

if __name__ == "__main__":
  main()