import json
import os

#name = input("Song name:")
#author = input("Artist:")
#file = input("url:")

url_path = "https://github.com/Nurufu/musicify-songs/raw/refs/heads/main/music/"

json_string = '{"latestVersion": "3.2.1", "indexName":"Apollo", "songs": []}'

data = json.loads(json_string)

directory = os.fsencode("music")

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    i = 0
    if filename.endswith(".dfpwm"):
        song = {"type":'song', "name": filename.replace('~', " "), "author": filename.replace('~', " "), "speed": 1, "file": url_path + filename}
        data["songs"].append(song)
        continue
    else:
        continue


with open('output.json', 'w') as file:
    json.dump(data, file, indent=4)