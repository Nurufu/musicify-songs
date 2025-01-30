import json
import os
import re

artist = r"\w.*(?= -)"
title = r"(?<=- )\w.*(?=.dfpwm)"

url_path = "https://github.com/Nurufu/musicify-songs/raw/refs/heads/main/music/"

json_string = '{"latestVersion": "3.2.1", "indexName":"Apollo", "songs": []}'

data = json.loads(json_string)

directory = os.fsencode("music")

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".dfpwm"):
        author = re.search(artist, filename.replace('~', " "))
        music = re.search(title, filename.replace('~', " "))
        song = {"type":'song', "name": music.group(0), "author": author.group(0), "speed": 1, "file": url_path + filename}
        data["songs"].append(song)
        continue
    else:
        continue


with open('output.json', 'w') as file:
    json.dump(data, file, indent=4)