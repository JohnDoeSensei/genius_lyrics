from lyricsgenius import Genius
from spotipy.oauth2 import SpotifyOAuth
import spotipy
from get_rapper_lyrics_from_wikipedia import get_rapper_fr

SPOTIFY_CLIENT_ID = '05ab690681b54cb492c222f808057a75'
SPOTIFY_CLIENT_SECRET = '41aadcd73fba4d4ea49d593e4ce2389a'
REDIRECT_URI = 'localhost:80'
genius = Genius('lETJKa6XhohQahDthANfDIsDwgz_NA-ZYjTHES6PCiSoXYcaHNNsFnBKDRRI_TdX')



#scope = "user-library-read"



#sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# After redirecting URI in localhost, copy url with code 
# Example : http://localhost/?code=AQBGuuEAsDkS8RwplYfdR3lqvyWm2qXQ4LMWoLVChRbnC0Z5312FpzSFUMr1rpjGqxCAZVUNL0kjCeFajVrPur6AueM9s-fYbSXJWCYH1ztjY_750UwnunkKeqnLYJg_Iyk8o2987MHv-nqOl1Zt3gSb_IJLxTsVD-OpPJ-cC8P7OBe9pYVCgA
# Paste the entire URL into prompt "Enter the URL you were redirected to": 

"""
rapper_fr = get_rapper_fr()
for rapper in rapper_fr :
    artist = genius.search_artist(rapper, max_songs=20, sort='title')
    #artist.add_song(artist.songs)
    json = artist.save_lyrics()
    print('[+] JSON lyrics saved from ', rapper, 'artist')
    #genius.save_artists(artist,filename=str(rapper)+'.json', overwrite=False)
"""

artist = genius.search_artist("Népal", max_songs=50, sort='popularity')
json_songs = artist.save_lyrics()
#print(json_songs.keys())
#df = clean_lyrics(df0,'lyric')
#Create the decades column
#df = create_decades(df)
#Filter  data to use songs that have lyrics.
#df = df[df['lyric'].notnull()]
#Save the data into a csv file
#df.to_csv('lyrics.csv',index=False)
#df.head(10)
    
