import re
import os

artist = r"\w.*(?= -)"
song = r"(?<=- )\w.*(?=.dfpwm)"

s = "AdhesiveWombat~-~Funky~Sundays.dfpwm"

x = re.search(artist, s.replace("~"," "))
xx = re.search(song, s.replace("~", " "))

print(x.group(0))
print(xx.group(0))
#artist = \w.*(?=- )
#song = (?<=- )\w.*(?=.dfpwm)