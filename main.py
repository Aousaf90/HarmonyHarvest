from tkinter import *
from tkinter import ttk
from pathlib import Path
from pytube import YouTube
import requests
def get_songs():
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
                    playlist_id = "3L0NJpTEIAfubSp7uUxcLq?si=3cce64c541694ca4"
                    endpoint = playlist_url + playlist_id + "/tracks"
                    params={'offset': 300, 'limit': 300}
                    # Send GET request to retrieve playlist data
                    get_response = requests.get(url=endpoint, headers=headers, params=params)

                    # Check for successful response
                    if get_response.status_code == 200:
                        spotify_data = get_response.json()
                        # print(f"Spotify Data = {spotify_data.keys()}")
                        playlist_name =  spotify_data['name']
                        tracks_detail = spotify_data['tracks']
                        tracks = tracks_detail['items']
                        print(f"Total number of Tracks = {len(tracks)}")
                        for track in tracks:
                            track_name = track['track']['name']
                            artist_name = track['track']['album']['artists'][0]['name']
                            songs_detail[track_name] = artist_name
                        #TODO: get the tracks items and then the tracks detail
                    else:
                        print(f"Error: {get_response.status_code}")
                else:
                    print(f"Error: {post_request.status_code}")
            return playlist_name, songs_detail
    except requests.exceptions.RequestException as e:
        RuntimeError(f"API request ERROR = {e}")
    return playlist_name, songs_detail

def download_video():
    pass

playlist_name = str()
songs_detail = dict()
playlist_name, songs_detail = get_songs()


print(f"Playlist = {playlist_name}")

for songs, artist in songs_detail.items():
    print(f"{songs}".rjust(10) + f" -------------->   {artist}".rjust(10))
# Tk = Tk()
# playlist_link = StringVar()
# canvas = Canvas(Tk, width= 100, height= 100)
# title = Tk.title("Harmony Harvest")
# input_label =  Label(Tk, text= "Playlist link", font= ('calibre', 50, 'bold'))
# playlist_link_windget= Entry(Tk, textvariable=playlist_link,font = ('calibre',50,'normal'))
# add_button =  Button(Tk, text= "Get Songs", command = gety
# _songs)
# input_label.pack()
# #Packing widgets
# add_button.pack()
# playlist_link_windget.pack()
# canvas.pack()
# Tk.mainloop()
 