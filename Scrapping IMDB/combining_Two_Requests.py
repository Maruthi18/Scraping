import requests
from bs4 import BeautifulSoup
from requests.models import Response

res = requests.get('https://www.imdb.com/chart/top/')

# print(res.status_code) # status code tell that whether we are getting the data are not

html = res.text

soup = BeautifulSoup(html, 'html.parser')

tbody = soup.find('tbody', {'class': 'lister-list'})
# print(table_body) # here we get everything inside the tbody tag

trs = tbody.findAll('tr')
for tr in trs:
	td = tr.find('td', {'class': 'titleColumn'})
	movie_id = td.a['href']
	movie_url = f'https://www.imdb.com/{movie_id}'

	res2 = requests.get(movie_url)
	html = res2.text
	soup2 = BeautifulSoup(html, 'html.parser')

	info = soup2.find('div', {'class': 'subtext'})
	# print(info.time.string.strip())

	# ---> when tags are more than one then this is not good to find out
	# ----> it will display first tag of the code
	# print(info.a.string)

	a = info.findAll('a')
	print(td.a.string)
	print(info.time.string.strip())

	# it is a list we can access through index number ,,,,,,,,,,,,,,,,

	# [<a href="/search/title?genres=drama&amp;explore=title_type,genres">Drama</a>, <a href="/title/tt0111161/releaseinfo" title="See more release dates">14 October 1994 (India)
	# </a>]
	print(a[0].string.strip())
	print(a[1].string.strip())

	print('<----------------------------->')
