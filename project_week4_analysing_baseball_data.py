"""for data analysis project_part 1"""

import csv

def read_csv_as_list_dict(filename, separator, quote):
    """reading csv file as list"""
    table = []
    with open(filename, newline = '') as csvfile:#reading opening csvfile
        reader = csv.reader(csvfile, delimiter = separator, quotechar = quote)#using csvreader
        for row in reader:
            table.append(row)#appending the values in list
    return table

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """reading csv file as nested dict"""
    table = {}
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = separator, quotechar = quote) #using Dict Reader to open the file in Dictionary form
        for row in reader:
            table[row[keyfield]] = row #appending each rows as key value pairs of dictionary
    return table

MINIMUM_AB = 500

def batting_average(info, batting_stats):
    """claculating batting average"""
    hits = float(batting_stats[info["hits"]]) #reading hits from dictionaries
    at_bats = float(batting_stats[info["atbats"]])#readinf at bats from dictionaries
    if at_bats >= MINIMUM_AB:
        return hits/at_bats #returning average
    else:
        return 0

def onbase_percentage(info, batting_stats):
    """calculating on_base percent"""
    hits = float(batting_stats[info["hits"]])#reading values
    at_bats = float(batting_stats[info["atbats"]])
    walks = float(batting_stats[info["walks"]])
    if(at_bats>=MINIMUM_AB):
        return (hits+walks)/(at_bats+walks)#calculating the onbase percentage
    else:
        return 0

def slugging_percentage(info, batting_stats):
    """calculating slugging percentage"""
    hits = float(batting_stats[info["hits"]])#reading values
    doubles = float(batting_stats[info["doubles"]])
    triples = float(batting_stats[info["triples"]])
    home_runs = float(batting_stats[info["home_runs"]])
    singles = hits-doubles-triples-home_runs
    at_bats = float(batting_stats[info["atbats"]])
    if at_bats>=MINIMUM_AB:
        return(singles+2*doubles + 3*triples + 4*home_runs)/ at_bats #calculating the percentage
    else:
        return 0

def filter_by_year(statistics, year, yearid):
    """arranging statistics by year"""
    result = []
    for row in (statistics):
        if row[yearid] == str(year):#searching values according to givern year
            result.append(row)#updating values
    return result

def top_player_ids(info, statistics, formula, numplayers):
    """calculating top players"""	
    player_ids = [] #declaring the list for palyers
    new_list =[]#declaring list for adding player tuples sorted in order
    formula_list =[]#having values of formulas computed
    top_players = []#list for returning the top players according to numplayers given
    for player in statistics:
        formula_value = formula(info, player)#calculating value
        player_ids.append(player[info['playerid']])#adding the required players
        formula_list.append(formula_value)#adding the values
        zipped = zip(player_ids, formula_list)#tupple
        new_list = sorted(zipped, key = lambda pair: pair[1], reverse = True)#sorting values
        top_players = new_list[:numplayers]#extracting according to top players
    return top_players

def lookup_player_names(info, top_ids_and_stats):
    """looking for player names by ids"""
    csv_file = read_csv_as_nested_dict(info["masterfile"], info["playerid"], 
               info["separator"], info['quote'])#reading required files
	
    players = list(csv_file)#listing the files to iterate through csv_file for names required
	
    firstname = [csv_file[players].get(info['firstname']) for players in csv_file]#searching firstnames of the players with given playerid
    lastname = [csv_file[players].get(info['lastname']) for players in csv_file]#searching lastnames of the players with given playerid
	
    dic = {}
    for lookup in range(len(players)):
        dic[players[lookup]] = firstname[lookup]+' '+lastname[lookup]#adding the firstname and last name in dictionary for playerids

    new = []
    for lookup in range(len(top_ids_and_stats)):
        new.append(str(format(top_ids_and_stats[lookup][1], '.3f'))
                 +' --- '+dic[top_ids_and_stats[lookup][0]])#adding values as required[x.xxx --- firstname lastname] in the list
    return new
	

def compute_top_stats_year(info, formula, numplayers, year):
    """cmputing statustics by year"""	
    stats = read_csv_as_list_dict(info["battingfile"], info["separator"], info["quote"])#required files
    stats_year = filter_by_year(stats, year, info["yearid"])#filtering by year
    player_ids = top_player_ids(info, stats_year, formula, numplayers)#looking for top ids according to the function before
    string = lookup_player_names(info, player_ids)#looking up thr player names
    return string#returning the required string

def aggregate_by_player_id(statistics, playerid, fields):
    """aggregating players of different fields"""
    new = {}
    for row in statistics:#choosing the dictionaries in statistics
        for values in fields:#choosing datas from the fields
            if row[playerid] in new.keys():#checking if playerid present in the keys of the rows
                if values in row.keys():#checking the values in row keys
                    new[row[playerid]][values] = new[row[playerid]].get(values, 0)+int(row[values])#appending the values if already present
            else:
                new[row[playerid]] = {playerid: row[playerid],values: int(row[values])}#if not present adding the player id alongwith values to add later
    return new


def compute_top_stats_career(info, formula, numplayers):
    """computing stats"""
    csv_file = read_csv_as_list_dict(info["masterfile"], info["separator"], info["quote"])#adding the required files
    aggregating = aggregate_by_player_id(csv_file, info["playerid"], info["battingfields"])#aggregating the files by already created function

    stats = []
    for players in aggregating:
        stats.append(aggregating[players])#adding the values
        top_notch = top_player_ids(info, stats, formula, numplayers)#checking the top players

    return lookup_player_names(info, top_notch)


