import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.imdb.com/chart/top/')
html = res.text

soup = BeautifulSoup(html , 'html.parser')

tbody = soup.find('tbody',{'class':'lister-list'})

trs = tbody.findAll('tr')

with open('imdbMovieRating.csv','w',encoding='utf-8') as f:
	for tr in trs:
		movieNametd = tr.find('td',{'class':'titleColumn'})
		ratingTd = tr.find('td',{'class' : 'ratingColumn'})
		f.write(movieNametd.a.string + " " + movieNametd.span.string + " " +ratingTd.strong.string)
		f.write('\n')

