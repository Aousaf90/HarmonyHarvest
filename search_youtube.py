# # api_key = "AIzaSyBTMTlc6y-kMZmgPDcXFa_bu39DGpEj7BY"
# # O_auth_client_id = ""
# inv = {
#     'Sword' : 1, 
#     'Potion' : 3
# }
# loot = {
#     'Sword' : 1, 
#     'Potion' : 10,
#     'Shield' : 1
# }
# new_inv = {
#     k : inv.get(k, 0) + loot.get(k, 0)
#     for k in set(inv | loot)
# }
# print(inv)
# __________________________
from pytube import YouTube
import urllib.request
import re
song_name = "We Don't Talk Anymore (feat. Selena Gomez"
song_artist = "Charlie Puth"
keyword = song_name +" "+ song_artist
keyword = keyword.split(" ")
if len(keyword) > 1:
    keyword = "+".join(keyword)
if "&" in keyword:
     keyword = keyword.replace("&", "%26")
print((keyword))
youtube_url = "https://www.youtube.com/results?search_query=" + keyword
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=cars")
print(type(html))
print(youtube_url)
# try:
#     link = input("Enter your video link : ")
#     video_ref = YouTube(link)
#     video = video_ref.streams.get_highest_resolution()
#     video.download()
#     print("Done")
# except:
#     print("There is some problem with the script")
try:
    pass
except:
    pass