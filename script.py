import json
import os

#name = input("Song name:")
#author = input("Artist:")
#file = input("url:")

json_string = '{"songs": []}'

data = json.loads(json_string)

directory = os.fsencode("music")

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    i = 0
    if filename.endswith(".dfpwm"):
        song = {"type":'song', "name": filename, "author": filename, "speed": 1, "file": "https://github.com/Nurufu/musicify-songs/raw/refs/heads/main/music/" + filename}
        data["songs"].append(song)
        continue
    else:
        continue


with open('output.json', 'w') as file:
    json.dump(data, file, indent=4)