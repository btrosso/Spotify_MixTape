import os
import spotipy
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials



# load_dotenv()

# date = input("What year would you like to travvel to? Type the date in this format YYYY-MM-DD: ")

URL = "https://www.billboard.com/charts/hot-100/2019-07-20/"

response = requests.get(URL)
top100_webpage = response.text

soup = BeautifulSoup(top100_webpage, "html.parser")

titles = soup.find_all(name="h3", id="title-of-a-story", class_="c-title")
titles_text = [title.getText().strip("\n") for title in titles]
rest = titles_text[5:len(titles_text)-16:4]
print(len(rest))
print(rest)




