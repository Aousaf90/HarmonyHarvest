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
import ssl
import re
song_name = "Mary On A Cross"
song_artist = "Ghost"
keyword = song_name +" by "+ song_artist
keyword = keyword.split(" ")
if len(keyword) > 1:
    keyword = "+".join(keyword)
if "&" in keyword:
     keyword = keyword.replace("&", "%26")
print((keyword))
youtube_url = "https://www.youtube.com/results?search_query=" + keyword
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
html = urllib.request.urlopen(youtube_url, context=context)
videos_result = re.findall(r"watch\?v=(\S{11})", html.read().decode())
video_url =  "https://www.youtube.com/watch?v=" + videos_result[0]
print(youtube_url)
print(video_url)
# print(html.read().decode())
try:
    video_ref = YouTube(video_url)
    video = video_ref.streams.get_highest_resolution()
    video.download()
    print("Done")
except Exception as e:
    print(e)
try:
    pass
except:
    pass