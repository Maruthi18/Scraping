import requests
from bs4 import BeautifulSoup

movieName = input("Enter Movie Name: ")

movieName = movieName.lower()

res = requests.get('https://www.imdb.com/chart/top/')

# print(res.status_code) # status code tell that whether we are getting the data are not

html = res.text

soup = BeautifulSoup(html, 'html.parser')

tbody = soup.find('tbody', {'class': 'lister-list'})
# print(table_body) # here we get everything inside the tbody tag

trs = tbody.findAll('tr')
for tr in trs:
	td = tr.find('td', {'class': 'titleColumn'})
	imdbMovieName = td.a.string.strip().lower()
	if imdbMovieName == movieName:
		movieId = td.a['href']
		movie_url = f'https://www.imdb.com/{movieId}'
		res2 = requests.get(movie_url)
		html = res2.text
		soup2 = BeautifulSoup(html, 'html.parser')
		summary = soup2.find('div', {'class': 'credit_summary_item'})
		dirId = summary.a['href']
		dirUrl = f'https://www.imdb.com/{dirId}'
		print("Dir Name ", summary.a.string)
		# print(dirUrl)
		res3 = requests.get(dirUrl)
		html = res3.text
		soup3 = BeautifulSoup(html, 'html.parser')
		knownfor = soup3.find('div', {'id': 'knownfor'})
		# print(knownFor)
		movieDivs = knownfor.findAll('div', {'class': 'knownfor-title'})

		for div in movieDivs:
			movieDiv = div.find('div', {'class': 'knownfor-title-role'})
			print(movieDiv.a.string)

# res2 --------------- < Director Name and Director Url > ---------------------------------------


# res3 ------------------ <  KnownFor > ----------------------
