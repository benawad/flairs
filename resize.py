from PIL import Image
import os

flairs = os.listdir('raw/')

for flair in flairs:
    im = Image.open('raw/' + flair)
    im.resize((52, 52)).save('resized/' + flair)

with open('flairs.txt', 'w') as f:
    f.write('\n'.join(sorted(flairs)))
