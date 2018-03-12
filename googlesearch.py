import requests, webbrowser, bs4

# asking for the value to search
search = input()

print('Googling...') # display text while downloading the Google page

#downloading the webpage containg the results
res = requests.get('http://google.com/search?q=' + search)
res.raise_for_status()

#scrapping the data from the downlaoded page
soup = bs4.BeautifulSoup(res.text)

#searching the required tags
linkElems = soup.select('.r a')


#choosing the top 5 links
numOpen = min (5, len(linkElems))

#displaying the links in the webbrowser
for i in range(numOpen):
	webbrowser.open('http://google.com'+ linkElems[i].get('href'))
