from requests import get
import json

#define URL that will be requested
url = 'https://www.siriusxm.com/40sJunction' #url you want to grab

#define the headers for the reqest of the JSON file
#taken from network inspecting the webpage
headers = {
'User-agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
'X-Requested-With': 'XMLHttpRequest',
'Referer': 'https://www.siriusxm.com/40sJunction',
'Host' : 'www.siriusxm.com',
'Accept-Encoding' : 'gzip, deflate, br',
'Accept' : 'application/json, text/javascript, */*; q=0.01',
'Accept-Language' : 'en-US,en;q=0.5',
'Connection' : 'keep-alive'
}

response = get(url) #request page and grab HTML

json = response.json()

