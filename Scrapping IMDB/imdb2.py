import requests
from bs4 import BeautifulSoup
res2 = requests.get('https://www.imdb.com//title/tt0111161/')
html = res2.text
soup2 = BeautifulSoup(html,'html.parser')

info = soup2.find('div',{'class':'subtext'})
print(info.time.string.strip())

# ---> when tags are more than one then this is not good to find out
# ----> it will display first tag of the code
print(info.a.string)

rating = info.findAll('a')

# it is a list we can access through index number ,,,,,,,,,,,,,,,, >
# [<a href="/search/title?genres=drama&amp;explore=title_type,genres">Drama</a>, <a href="/title/tt0111161/releaseinfo" title="See more release dates">14 October 1994 (India)
# </a>]
print(rating[0].string)
print(rating[1].string)