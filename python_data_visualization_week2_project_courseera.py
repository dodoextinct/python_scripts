"""plotting gdp datas"""
import csv
import pygal

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """reading files as nested dictionaries"""

    #adding new dictionary
    new={}
    
    #opening the file
    with open(filename, newline='') as csvfile:
        #using csv dictionary reader 
        reader = csv.DictReader(csvfile, delimiter = separator, quotechar = quote)
	#reading each file
        for row in reader:
            new[row[keyfield]] = row

    return new

def build_plot_values(gdpinfo, gdpdata):
    """building plot values from dictionaries recieved"""

    #intitalising the lists
    new = []
    year = []
    gdp = []

    #iterating each key in gdpdata
    for keys in gdpdata.keys():
	#innitalizing values of the keys
        data = gdpdata[keys]
	#check if data is null or not
        if data != '':
	    #check if data lies in between the required range
            if int(keys) in range(gdpinfo["min_year"], gdpinfo["max_year"] + 1):
		
		#adding datas
                year.append(int(keys))
                gdp.append(float(gdpdata.get(keys)))
		
		#zipping value in tupples
                zipped = zip(year, gdp)
		
		#adding those tupples in list as zipped values
                new = list(sorted(zipped))
			
    return new

def build_plot_dict(gdpinfo, country_list):
    """building dictionary for dictionary"""
    dictionary = {}
    
    #reading the required lists
    gdp = read_csv_as_nested_dict(gdpinfo["gdpfile"], gdpinfo["country_name"],
                gdpinfo["separator"], gdpinfo["quote"])

    #popping values
    for value in gdp.values():
        value.pop(gdpinfo["country_name"])
        value.pop(gdpinfo["country_code"])

    #adding required values and building the dictioary
    for names in country_list:
        dictionary[names] = []
        for key, values in gdp.items():
            if key == names:
                tup = build_plot_values(gdpinfo, values)
                dictionary[names] = tup
    return dictionary 

def render_xy_plot(gdpinfo, country_list, plot_name):
    """plotting..."""
    dic = build_plot_dict(gdpinfo, country_list)

    #using the pygal module for plotting
    chart = pygal.XY()
	
    for country in country_list:
        years = []
        for item in dic[country]:
            years.append((pygal.datetime.date(item[0],1,1), item[1]))
            chart.add(country, years)

    chart.render_to_file(plot_name)

		
		
