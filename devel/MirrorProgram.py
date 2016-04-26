import os
from PIL import Image

for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
       continue
    
    im = Image.open(filename)
    im.transpose(Image.FLIP_LEFT_RIGHT).save('mirror.png')
