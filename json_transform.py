import json
import pandas as pd

# https://towardsdatascience.com/how-to-analyze-emotions-and-words-of-the-lyrics-from-your-favorite-music-artist-bbca10411283


df = pd.DataFrame(columns=['release_date','artist','title','album','lyrics'])
with open('Lyrics_Népal.json') as f :
    lyrics = json.load(f)
    songs = lyrics['songs']
    for e in songs :
        pass
        
    for s in songs : 
        #print(s.keys())
        if s['album'] == None :
            album = 'none'
        else: 
            album = s['album']['name']
        print(s['album'])
        lyrics = s['lyrics']
        
        artist = 'Népal'
        title_song = s['title']
        date = s['release_date']
        new_row = {
            'release_date':date ,
            'artist':artist,
            'title':title_song,
            'album':album,
            'lyrics':lyrics
        }
        df = df.append(new_row,ignore_index=True)

df.to_csv('Nepal.csv')
        
        #print(lyrics)