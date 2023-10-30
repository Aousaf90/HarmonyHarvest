from tkinter import *
from tkinter import ttk
from pathlib import Path
import requests
import re
import pandas
def get_songs():
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
                post_request = requests.post(url= post_url, headers=post_request_header,data= post_request_data )
                if post_request.status_code == 200:
                    print("API CONNECTED SUCCESSFULLY")
                    DATA = post_request.json()
                    access_token = DATA['access_token']
                    get_request  = {
                        "Authorization": access_token
                    }
                    playlist_url = "https://open.spotify.com/playlist/"
                    playlist_id = "3L0NJpTEIAfubSp7uUxcLq?si=5b9b7c124a4d4812"
                    # TODO: use re instead of simple striping
                    # playlist_id =  playlist_url.split("/")[-1]
                    print("Playlist URl: ", playlist_id)
                    get_response = requests.get(url=playlist_url+playlist_id, headers=get_request)
                    if get_response.status_code == 200:
                        print("SPOTIFY DATA GET SUCCESSFULLY")
                    else:
                        print("THERE WAS AN ERROR")
                        print("ERROR CODE: ", get_response.status_code)
    except requests.exceptions.RequestException as e:
        print("NO request Get")
        print(f"API request ERROR = {e}")
get_songs() 
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
