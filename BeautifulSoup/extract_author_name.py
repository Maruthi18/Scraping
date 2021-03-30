import requests
from bs4 import BeautifulSoup
res = requests.get('https://quotes.toscrape.com/')
html = res.text

soup = BeautifulSoup(html , 'html.parser')
with open('extract_author_name.csv','w',encoding='utf-8') as f:
	for tag in soup.findAll('small',{'class' : 'author'}):
		f.write(tag.string)
		f.write('\n')
		
	

