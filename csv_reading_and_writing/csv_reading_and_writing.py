import csv

def read_csv(filename):
	"""reads csv files and adds the data to a table"""

	with open(filename, newline='') as csvfile: #opening files as csv files
		table = []
		reader = csv.reader(csvfile) #using csv reader to read the files
		for row in reader:
			table.append(row) #adding values to the table
	return table

def write_csv(csv_table, file_name):
	"""writing csv files from tables"""	

	with open(file_name, 'w', newline='') as csvfile: #creating a csvfile
		csv_writer = csv.writer(csvfile)
		for row in csv_table:
			csv_writer.writerow(row) #using csv default function to write values

def print_table(table):
	"""printing values"""
	for row in table:
		print(row)

def test_code():
	"""testing values"""
	test = read_csv("test_case.csv")
	print_table(test)
	print()

	cancer_risk = read_csv("cancer_risk.csv")
	write_csv(cancer_risk, "cancer_risk_copy.csv")
	cancer_risk_copy = read_csv("cancer_risk_copy.csv")

	print(cancer_risk == cancer_risk_copy) #will return true if wrote correctly and copied correctly


test_code()
	
