"""webscrapping data"""

#importing neccesaary libraries
import requests, bs4,csv

#opening the desired website
res = requests.get("https://www.mapsofindia.com/election/list-of-portfolios.html")
res.raise_for_status()

#scrapping the data
soup = bs4.BeautifulSoup(res.text, "lxml")

#required table needed
tables = soup.find("table",attrs={"cellspacing":"0","cellpadding":"2","border":"1","align":"center","width":"98%","style":"background-color:#F5F3F4;text-align:left;"})

#dictionaries of words
info = ['information', 'finance','commerce', 'industry','statistics',
	'technology','electronics','civil','human','planning','employment','science']

#initialsing dictionary
res = []

#finding the rows that have tr tag
for row in tables.findAll("tr"):
	#all those with id tag
	cells = row.findAll("td")

	#selecting the tags those have all the values needed
	if len(cells) == 3:
		
		#separating values by commas
		for ministiries in cells[1].getText().split(","):
			#separating values by spaces				
			names = ministiries.split(" ")
			#checking every string
			for strings in names:
				#checking if value is present in the required set or not
				if strings.lower() in info:
					#avoiding duplication
					if cells[1].getText() not in res:
						res.append(cells[1].getText())
						#writing values in csv file
						with open('my.csv', 'a') as csvfile:
							writer = csv.writer(csvfile, delimiter = ',')
							writer.writerow([cells[1].getText(),cells[2].getText()])







	


	

