from PIL import Image
import json
import os

flairs = os.listdir("raw/")

for flair in flairs:
    if flair.endswith(".png"):
        im = Image.open("raw/" + flair)
        im.resize((52, 52)).save("resized/" + flair)

resized_flairs = os.listdir("resized/")

with open("flairs.txt", "w") as f:
    f.write("\n".join(sorted(resized_flairs)))

with open("map.js", "w") as f:
    d = {}
    for flair in resized_flairs:
        d[flair.split(".")[0]] = flair
    f.write("export const flairMap = " + json.dumps(d))
