import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

Client_ID="796ad901a3044ff5bbc219ed0550317b"
Client_secret="a2421b95e41c482e87887c957254bf45"


date = input("Which time would you like to time travel Enter the date in the format YYYY-MM-DD : ")

response=requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
response_text=response.text 

soup=BeautifulSoup(response_text,"html.parser")
song_title=soup.select("li ul li h3")
song_name=[]
for i in song_title:
    song_name.append(i.getText().strip())


sp=spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id=Client_ID,
        client_secret=Client_secret,
        redirect_uri="http://example.com/",
        show_dialog=True,
        cache_path="token.txt",
        username=f"100 song of {date}"
        

    ))

user_id=sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]

# print(song_name)
for song in song_name:
    result=sp.search(q=f"track:{song} year:{year}",type="track")
    try:
        uri=result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} is not available in spotify")
        
playlist=sp.user_playlist_create(user_id,name=f"{date} Billboard 100",public=False)

sp.playlist_add_items(playlist_id=playlist["id"],items=song_uris)
