import os#Imports os so it can search folders
from PIL import Image

for filename in os.listdir('.'):#Searches directories
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \#Selects images
       continue
    
    im = Image.open(filename)#Sets a value to the images
    im.transpose(Image.FLIP_LEFT_RIGHT).save('mirror.png')#It flips the image and saves it
