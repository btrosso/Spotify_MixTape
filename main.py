import json
import os
import spotipy
import requests
import pprint
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials



load_dotenv()
pp = pprint.PrettyPrinter()
# date = input("What year would you like to travvel to? Type the date in this format YYYY-MM-DD: ")

URL = "https://www.billboard.com/charts/hot-100/2019-07-20/"
SPOT_SEARCH_URL = "https://api.spotify.com/v1/search/"
SPOT_HEADER = {
    "Authorization": f"Bearer {os.environ['SPOTIFY_TOKEN']}",
    "Content-Type": "application/json"
}

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=os.environ["SPOTIFY_CLIENT_ID"],
        client_secret=os.environ["SPOTIFY_CLIENT_SECRET"],
        show_dialog=True,
        cache_path="token.txt"
    )
)

response = requests.get(URL)
top100_webpage = response.text

soup = BeautifulSoup(top100_webpage, "html.parser")

found_titles = soup.find_all(name="h3", id="title-of-a-story", class_="c-title")
found_titles_text = [title.getText().strip("\n") for title in found_titles]
titles_list = found_titles_text[5:len(found_titles_text)-16:4]
# print(len(titles_list))
print(titles_list)

user_id = sp.current_user()["id"]
uri_list = []
for title in titles_list:
    result = sp.search(q=f"track: {title} year: {2019}", limit=1, type="track")
    # print(result)
    try:
        uri_list.append(result['tracks']['items'][0]["uri"])
        print(result['tracks']['items'][0]["uri"] + ": added to list!")
    except IndexError:
        print(f"{title} doesn't exist in Spotify. Skipped.")

