from tkinter import *
from tkinter import ttk
from pathlib import Path
import requests
import pandas
def get_songs():
    print(requests.get(""))
    
    url  = "https://api.spotify.com."
    try:
        if url.strip():
            response = requests.get(url)
            print(response.json())
    except requests.exceptions.RequestException as e:
        print("NO request Get")
        print(f"ERROR Making = {e}")
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
