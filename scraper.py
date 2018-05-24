import requests, json, datetime, openpyxl, time 

#get_current_song()
def get_current_song(): #gets song artist, album and name

    json_time = datetime.datetime.now(datetime.timezone.utc).strftime('%m-%d-%H:%M:00') #website uses UTC in this format for the json files that are updated at the top of every minute

    url = "https://www.siriusxm.com/metadata/pdt/en-us/json/channels/8205/timestamp/" + str(json_time) #the json url of the current song playing 
 
    r = requests.get(url) #request page and grab HTML

    if r.status_code == 200: #if request is successful

        json = r.json() #get the json file from the request and decode it

        json_dicts= json['channelMetadataResponse']['metaData']['currentEvent'] #json dictonarys containing all the info
        artist = json_dicts['artists']['name'] #grab the name
        album = json_dicts['song']['album']['name'] #grab album
        song = json_dicts['song']['name'] #grabe song
        
        return artist, album, song 
    else:
        return 'request did not go through'

#create a unique song id made up of the song name and artist
def song_id_gen(song):
    return str(song[2]) + '-' + str(song[0]) #song ids are used to allow for songs with the same name but by diffrent artist

#write song to workbook
def song_to_xlsx(song):
    wb = openpyxl.load_workbook('songs.xlsx') #open song workbook
    sheet = wb['Sheet1'] #open sheet one
    row = str(sheet.max_row + 1) #row to right on is one greater than the last written one
    sheet['A' + row].value = song[0] #write artist in column a
    sheet['B' + row].value = song[1] #write album in column b
    sheet['C' + row].value = song[2] #write song in comlumn c
    sheet['D' + row].value = song_id_gen(song) #write song id in comlumn d

    wb.save('songs.xlsx') #Save workbook

#workbook column to list
def column_to_list(column):
    output = []
    wb = openpyxl.load_workbook('songs.xlsx') #open song workbook
    sheet = wb['Sheet1'] #open sheet one
 
    for i in range(sheet.max_row - 1): #for the entire sheet - 1 one because we want to leave the titles alone
        output.append(sheet[str(column)+str(i+2)].value) #out put the value of the cell, +2 to avoid title cells

    return output


used_songs = column_to_list('D') #all the songs that have been recorded ids
exit = False


while exit == False: #while exit is not true
    if datetime.datetime.now(datetime.timezone.utc).strftime('%S') == '00': #if it is the top of the minute
        if song_id_gen(get_current_song()) in used_songs: #if the songs id has been used before, dont record it 
            print('song has been recorded')
        else: #if song has not been seen before
            song_to_xlsx(get_current_song()) #write the song to the excel sheet
            print(song_id_gen(get_current_song()))
            used_songs.append(song_id_gen(get_current_song())) #add song id to used songs
        time.sleep(59)
