from tkinter import *
from tkinter import ttk
from pytube import YouTube
import requests
import re
import urllib.request
import ssl
import os

def get_songs(playlist_url = ""):

    playlist_id = playlist_url.split("/")[-1]
    playlist_name = str()
    songs_detail = dict()
    url  = "https://api.spotify.com."
    try:
        if url.strip():
            response = requests.get(url)
            status_code = response.status_code
            if status_code == 200:
                post_url = "https://accounts.spotify.com/api/token"
                post_request_header = {"Content-Type": "application/x-www-form-urlencoded"}
                post_request_data = {
                    "grant_type":"client_credentials",
                    "client_id": "fd7fca6bd4824b0091280fb695cd4441",
                    "client_secret": "f94dc958f9174aaaade597dfa444775a" 
                }
                
                post_request = requests.post(url = post_url, headers = post_request_header, data = post_request_data )
                if post_request.status_code == 200:
                    print("API CONNECTED SUCCESSFULLY")
                    DATA = post_request.json()
                    access_token = DATA['access_token']

                    # Prepare headers for GET request
                    headers = {
                        'Authorization': 'Bearer ' + access_token,
                        'Accept': 'application/json'
                    }
                    # Construct playlist URL
                    playlist_url = "https://api.spotify.com/v1/playlists/"
                    endpoint = playlist_url + playlist_id + "/tracks"
                    params={'offset': 300, 'limit': 300}
                    # Send GET request to retrieve playlist data
                    get_response = requests.get(url=endpoint, headers=headers, params=params)

                    # Check for successful response
                    if get_response.status_code == 200:
                        spotify_data = get_response.json()
                        playlist_name =  spotify_data['name']
                        tracks_detail = spotify_data['tracks']
                        tracks = tracks_detail['items']
                        for track in tracks:
                            track_name = track['track']['name']
                            artist_name = track['track']['album']['artists'][0]['name']
                            songs_detail[track_name] = artist_name
                    else:
                        print(f"Error: {get_response.status_code}")
                else:
                    print(f"Error: {post_request.status_code}")
            return playlist_name, songs_detail
    except requests.exceptions.RequestException as e:
        RuntimeError(f"API request ERROR = {e}")
    return playlist_name, songs_detail


def search_youtube(songs, artist):
    keyword = songs +" by "+ artist
    keyword = keyword.split(" ")
    if len(keyword) > 1:
        keyword = "+".join(keyword)
    if "&" in keyword:
        keyword = keyword.replace("&", "%26")
    youtube_url = "https://www.youtube.com/results?search_query=" + keyword
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    html = urllib.request.urlopen(youtube_url, context=context)
    videos_result = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    video_url =  "https://www.youtube.com/watch?v=" + videos_result[0]
    return video_url


def download_video(playlist_folder, song,video_url):
    try:
        video_ref = YouTube(video_url)
        video = video_ref.streams.get_highest_resolution()
        video.download(output_path= f"{playlist_folder}/")
        print(f"{song} downloaded successfully")
    except Exception as e:
        print(e)

url = "https://open.spotify.com/playlist/4vliiojT3JgFCBUCHhNzeD?si=19c2219665234f40"
playlist_name, songs_detail = get_songs(url)
print(f"Getting Data for ( {playlist_name} ) playlist")
os.remove(playlist_name) if os.path.exists(playlist_name) else os.makedirs(playlist_name)
for songs, artist in songs_detail.items():  
    video_url =  search_youtube(songs, artist)
    download_video(playlist_name, songs, video_url)