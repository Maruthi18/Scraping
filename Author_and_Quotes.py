import requests


for i in range (1, 11):
	print (i)
	res = requests.get (f'https://quotes.toscrape.com/page/{i}/')
	html = res.text

	with open ('Author_quotes.csv', 'a', encoding='utf-8') as f:
		for line in html.split ('\n'):
			if '<span class="text" itemprop="text">' in line:
				line = line.replace ('<span class="text" itemprop="text">“', '').replace ('”</span>', '')
				quotes = line.strip ()


			if '<span>by <small class="author" itemprop="author">' in line:
				line = line.replace ('<span>by <small class="author" itemprop="author">', '').replace ('</small>', '')
				author = line.strip ()

				# author = line.replace("<span = 'https://quotes.toscrape.com/page/{i}'")

				print (f'{author} , {quotes}\n')

				f.write (f'{author} , {quotes}\n')

				f.write ('\n')
