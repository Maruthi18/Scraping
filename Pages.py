import requests
for i in range(0,11):
	print("Pages : " , i)
	url = f'https://quotes.toscrape.com/page/{i}/'
	r = requests.get(url)
	html = r.text
	with open('quotes.txt','w',encoding='utf-8') as f :
		for line in html.split('\n'):
			if '<span class="text" itemprop="text">' in line:
				line = line.replace('<span class="text" itemprop="text">“',"").replace('”</span>','')
				line = line.strip()
				print(line)
				f.write(line)
				f.write('\n')