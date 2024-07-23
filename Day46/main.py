from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import pprint

print(
    """
████████╗██╗███╗░░░███╗███████╗  ███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗
╚══██╔══╝██║████╗░████║██╔════╝  ████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝
░░░██║░░░██║██╔████╔██║█████╗░░  ██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░
░░░██║░░░██║██║╚██╔╝██║██╔══╝░░  ██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░
░░░██║░░░██║██║░╚═╝░██║███████╗  ██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗
░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝
    """
)
desired_year = input("What year would you like to travel to? (Enter the date using this format YYYY-MM-DD): ")

# Scrape the top 100 song titles from Billboard Hot 100
response = requests.get(F"https://www.billboard.com/charts/hot-100/{desired_year}/")

bill_page = response.text
soup = BeautifulSoup(bill_page, "html.parser")

top_100 = soup.select("li h3#title-of-a-story")
top_100_titles = [title.getText().replace('\n', '').replace('\t', '').replace('\\', '') for title in top_100]
print("\nThe Billboard Hot 100 are:")
pprint.pp(top_100_titles)

# Connect to Spotify
client_ID = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_URI = os.getenv("REDIRECT_URI")

scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_ID, client_secret=client_secret, redirect_uri=redirect_URI, scope=scope))
user = sp.current_user()

# Search songs on spotify
songs_URI = []
count = 0
for title in top_100_titles:
    try:
        uri = sp.search(
            q=f"track:{title} year:{desired_year[:4]}",
            type="track",
        )
        track_uri = uri['tracks']['items'][0]["uri"]
    except Exception as e:
        print(f"\nAn error occurred while searching for the song - {top_100_titles[count]}: {e}")
    else:
        songs_URI.append(track_uri)
    count += 1
print(f"\nSongs found on Spotify and URIs saved to list.")

# Create the Spotify playlist
playlist = None
try:
    playlist = sp.user_playlist_create(
        user=f"{user['id']}",
        name=f"{desired_year} Billboard 100",
        public=False,
        description=f"The Billboard 100 songs from {desired_year}."
    )
except Exception as e:
    print(f"\nAn error occurred while creating the playlist: {e}")
else:
    print("\nPlaylist Information\n********************")
    pprint.pp(playlist)

# Add songs to the Spotify playlist
try:
    add_tracks = sp.playlist_add_items(
        playlist_id=f"{playlist['id']}",
        items=songs_URI
    )
except Exception as e:
    print(f"\nAn error occurred while adding songs to the playlist: {e}")
else:
    print(f"\nTracks added successfully - {add_tracks}")
