# 40s_scraper
![alt-text](http://www.essexmobiledisco.co.uk/images/40s.jpg)

### Introduction

 Welcome to my first somewhat legit Github project.  
 
   The gist of the project is that I'm a sucker for 40s big band and swing and the best source of said music that I've found was Siruis XM's 40s Junction.  The issue is Siruis XM is a paid subscription-based service and why pay a service I could replicate myself.  

### How it works
   Sirius XM has a website that shows the current song being played for each channel.  In this case I was interested in the [40s Juction channel webpage](https://www.siriusxm.com/40sJunction). The _scraper.py_ script, at the top of every minute UTC time, requests the JSON file from Sirius XM.  This the same interval that a web browser would request the JSON. The script then grabs the current song title and artist name from said JSON and stores them as variables.  
