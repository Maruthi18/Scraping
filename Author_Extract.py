import requests
res = requests.get("https://quotes.toscrape.com/")
html = res.text  # html convert into text format

with open('Authors.txt','w') as f:
	for line in html.split('\n'):  # html converting into list (and) at every end of code line add a \n (and) every line of html code converted into list element eg ['<head>'],['<\head>']
		if '<small class="author" itemprop="author">' in line:
			line = line.replace('<span>by <small class="author" itemprop="author">','') # here string replace with '' empty string
			line = line.replace('</small>','') # here also same step
			author = line.strip() # remove white spaces
			print(author)
			f.write(author)
			f.write('\n')
