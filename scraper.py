import requests

#define URL that will be requested
#url = 'https://www.siriusxm.com/40sJunction' #url you want to grab
url = 'https://www.siriusxm.com/metadata/pdt/en-us/json/channels/8205/timestamp/05-23-01:03:00'

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

r = requests.get(url, headers = headers) #request page and grab HTML

print('status code: ' + str(r.status_code))

json = r.json()

print(json)
