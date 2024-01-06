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
from pytube import YouTube
try:
    link = input("Enter your video link : ")
    video_ref = YouTube(link)
    video = video_ref.streams.get_highest_resolution()
    video.download()
    print("Done")
except:
    print("There is some problem with the script")