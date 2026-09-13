# Import yandex music api, .env manager, requests and genius lyrics api
from yandex_music import Client
import lyricsgenius
from requests import get
from os import getenv
from dotenv import load_dotenv
load_dotenv()

# Initialize genius and yandex music clients 
genius = lyricsgenius.Genius(getenv("genius_access_token"))
client = Client(token=getenv("yandex_token"))
client.init()



# get song lyrics from genius api by search
def genius_search_lyrics(query):
    song = genius.search_song(query)
    if song:
        return song.lyrics
    return None

# format array of artists to string
def artists_array_to_string(artists):
    result = ""
    for a in artists:
        result += a.name + ", "
    return result.strip(", ")

# get Track instance by it's id
def find_track_by_id(id):
    return client.tracks(id)[0]

# get lyrics (multi-line string). From yandex music if exists, else from genius
def get_lyrics(info):
    if info["has_yandex_lyrics"]:
        track = find_track_by_id(info['id'])
        return get(track.get_lyrics().download_url).text
    else:
        return genius_search_lyrics(f"{info['artists']} {info['title']}")
    
# format Track instance to readable json
def get_track_info(track):
    return {
        "title":track.title,
        "artists": artists_array_to_string(track.artists),
        "color": track.derived_colors.average,
        "cover": track.get_cover_url(),
        "has_yandex_lyrics":track.lyrics_info.has_available_text_lyrics,
        "id":track.id
    }

# returns array of jsons for each track found by query
def search(query):
    search_results = client.tracks(track_ids=[c["id"] for c in client.search(query)["tracks"]["results"]])
    tracks = []
    for track in search_results:
        tracks.append(get_track_info(track))
    return tracks

# test search module
if __name__ == "__main__":
    test_query = "Rick Astley - Never Gonna Give You Up"
    results = search(test_query)
    print(results[0])
    print(get_lyrics(results[0]))