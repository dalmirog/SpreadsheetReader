build:
	docker build -t dalmirog/spreadsheetreader:latest .
run:
	docker run -p 80:80 \
           -e SPREADSHEETID="1DV-eajMmYxksh1JFdn-LJQ_y8RgdbFBh_-u-vF1hVXA" \
           -e SPREADSHEETNAME="Data" \
           -e COLUMNRANGE="A2:C" \ 
           dalmirog/spreadsheetreader:latest

		# TODO move this to local environment variables 