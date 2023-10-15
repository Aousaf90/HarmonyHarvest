from tkinter import *
from tkinter import ttk
from pathlib import Path
import pandas
def get_songs():
    pass

Tk = Tk()
playlist_link = StringVar()
canvas = Canvas(Tk, width= 100, height= 100)
title = Tk.title("Harmony Harvest")
input_label =  Label(Tk, text= "Playlist link", font= ('calibre', 50, 'bold'))
playlist_link_windget= Entry(Tk, textvariable=playlist_link,font = ('calibre',50,'normal'))
add_button =  Button(Tk, text= "Get Songs", command = get_songs)
#Packing widgets
input_label.pack()
add_button.pack()
playlist_link_windget.pack()
canvas.pack()
Tk.mainloop()
