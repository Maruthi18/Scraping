import requests
from bs4 import BeautifulSoup

res = requests.get ('https://www.imdb.com/chart/top/')

# print(res.status_code) # status code tell that whether we are getting the data are not

html = res.text

soup = BeautifulSoup (html, 'html.parser')

tbody = soup.find ('tbody', { 'class': 'lister-list' })
# print(table_body) # here we get everything inside the tbody tag

trs = tbody.findAll ('tr')
for tr in trs :
	td = tr.find ('td', {'class': 'titleColumn'})
	print(td.a.string)
