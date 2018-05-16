from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.siriusxm.com/40sJunction'

page = urlopen(url)

parsed_page = BeautifulSoup(page, "html.parser")

#find artist
#artist_box = parsed_page.find('div', attrs={'id' : 'onair-pdt'})
artist_box = parsed_page.find('p', attrs={'id' : 'onair-pdt'})
artist = artist_box.text.strip()
print(artist_box)

