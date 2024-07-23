from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

desired_year = input("What year would you like to travel to? (Enter the date using this format YYYY-MM-DD): ")

# scrape the top 100 song titles from Billboard Hot 100
response = requests.get(F"https://www.billboard.com/charts/hot-100/{desired_year}/")
# response = requests.get(F"https://www.billboard.com/charts/hot-100/1999-07-10/")

bill_page = response.text

soup = BeautifulSoup(bill_page, "html.parser")

top_100 = soup.select("li h3#title-of-a-story")
top_100_titles = [title.getText().replace('\n', '').replace('\t', '') for title in top_100]
print(top_100_titles)

# Connect to Spotify
client_ID = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
