# 40s_scraper
![alt-text](http://www.essexmobiledisco.co.uk/images/40s.jpg)

### Introduction

 Welcome to my first somewhat legit Github project.  
 
The gist of the project is that I'm a sucker for 40s big band and swing and the best source of said music that I've found was Siruis XM's 40s Junction.  The issue is Siruis XM is a paid subscription-based service and why pay a service I could replicate myself.  

### How it works
Sirius XM has a website that shows the current song being played and its information for each channel.  In this case I was interested in the [40s Juction channel webpage](https://www.siriusxm.com/40sJunction). The _scraper.py_ script, at the top of every minute UTC time, requests the 40s Junciton JSON file from Sirius XM.  This the same interval that a web browser would request the JSON. The script then grabs the current song title, artist name, and album name from said JSON and stores them as variables. _scraper.py_  then stores the song information in a _songs.xlsx_ file (Microsoft Excel file) because I do not know SQL.  Along with the song information, a link to the first YouTube video after a query of the song title and artist name is added to the _songs.xlsx_ file.  This of course can lead to not the best quality videos for sound but at least it gives a starting point. The _scraper.py_ script can continue to run, gathering song information and videos along the way, until the user stops the script.

After gathering the song information with _scraper.py_, use _download.py_ to download the audio of the YouTube videos using _songs.xlsx_.  _download.py_ uses the _youtube-dl_ and _mutagen_ module to download the _.mp3's_ from the YouTube videos and label them respectivly. 
