import os#Imports your os so it can browse your folders
from PIL import Image

LOGO_FILENAME = 'Logo.png'#This sets the name the logo should have and what it looks for

logoIm = Image.open(LOGO_FILENAME)#This part sets the value of the logo
logoWidth, logoHeight = logoIm.size#This sets a value to the logo size
im = Image.open(filename)#This sets a value to the image
width, height = im.size#This sets a value to the image size

os.makedirs('withLogo', exist_ok=True)#This will make a directory that ends the name of the image with 'withLogo'
for filename in os.listdir('.'):#This searches the directory
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \#This sets it so it searches for filenames that images usually are
       or filename == LOGO_FILENAME:#This looks for the logo
        continue 

print('Adding logo to %s...' % (filename))#This tells you that it has started to add the logo
im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)#Pastes the logo to the image
im.save(os.path.join('withLogo', filename))#Saves the image with the logo attached
