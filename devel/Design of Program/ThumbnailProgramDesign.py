import os#Imports os to browse directories
from PIL import Image

SmallSize = 300#Sets a max size that it uses to shrink image

os.makedirs('Thumbnail', exist_ok=True)#Creats a directory for the images to be saved in
for filename in so.listdir('.'):#Searches files
    if not (filename.endswith('.png') or filename.endswith('.jpg'))\#Searches for the filenames
       or filename == Logo:#Also selects logos
        continue

im = Image.open(filename)#Sets a value to the image
width, height = im.size#sets a value to the size
if width > SmallSize and height > SmallSize:#Checks to make sure the size is larger than the max size
    if width > height:#Checks if the width is larger than the height
        height = int((SmallSize / width) * height)#If so it divides the width by 300 and then multiplies by the height
        width = SmallSize #It then sets the width to 300
    else:
        width = int((SmallSize / height) * width)#Otherwise it does the opposite
        height = SmallSize

    print('Resizing %s...' % (filename))#Tells you its resizing
    im = im.resize((width,height))#Sets a value to the resized size

im.save(os.path.join('Thumbnail', filename))#Then it saves the image and adds Thumbnail to the end
