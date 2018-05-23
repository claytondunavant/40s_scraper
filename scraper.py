import requests, json, datetime

def get_current_song(): #gets song artist, album and name
    json_time = datetime.datetime.now(datetime.timezone.utc).strftime('%m-%d-%H:%M:00') #website uses UTC in this format for the json files that are updated at the top of every minute

    url = "https://www.siriusxm.com/metadata/pdt/en-us/json/channels/8205/timestamp/" + str(json_time) #the json url of the current song playing 
 
    r = requests.get(url) #request page and grab HTML

    json = r.json() #get the json file from the request and decode it

    json_dicts= json['channelMetadataResponse']['metaData']['currentEvent'] #json dictonarys containing all the info
    artist = json_dicts['artists']['name'] #grab the name
    album = json_dicts['song']['album']['name'] #grab album
    song = json_dicts['song']['name'] #grabe song

    return artist, album, song
   
print(get_current_song())
