from bs4 import BeautifulSoup
import requests
from ytmusicapi import YTMusic
from pprint import pprint
import os

date = input("Which year do you want to travel to ? Type the date in this format YYYY-MM-DD: ")
URL = os.environ["CHART_URL_TEMPLATE"].format(date=date)

response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

songs = soup.find_all(name="h3", class_="chart-entry__title")

song_names = [song.get_text() for song in songs]

print(song_names)

yt = YTMusic("browser.json")
playlists = yt.get_library_playlists()
print(f"Found {len(playlists)} playlists in your library.")

playlist_id = yt.create_playlist(
    title=f"Chart songs for {date}",
    description="Date-based chart playlist created with Python",
    privacy_status="PRIVATE"
)

video_ids = []

for song in song_names:
    results = yt.search(song, filter="songs", limit=1)

    if results:
        video_ids.append(results[0]["videoId"])

print(f"Found {len(video_ids)} songs")

result = yt.add_playlist_items(
    playlistId=playlist_id,
    videoIds=video_ids
)

pprint(result)





