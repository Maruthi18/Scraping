from bs4 import BeautifulSoup
import requests

r = requests.get ('https://quotes.toscrape.com/')
html = r.text
soup = BeautifulSoup (html, 'html.parser')
# print (type (soup))
# print (soup.span)  # it will provide you first apperance of span in html code
# print (soup.title.string)
# title convert into html code to string

# print (soup.title.parent)

# print (soup.findAll ('a'))  # here we got all span tag in html code

# for tag in soup.findAll('a'):
# 	print(tag)
with open('bs4Quotes.txt','w',encoding='utf-8') as f:
	for tag in soup.findAll ('span', { 'class': 'text' }):
		f.write(tag.string)
		f.write('\n')
