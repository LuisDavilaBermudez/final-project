import os
from PIL import Image

SmallSize = 300

os.makedirs('Thumbnail', exist_ok=True)
for filename in so.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg'))\
       or filename == Logo:
        continue

im = Image.open(filename)
width, height = im.size
if width > SmallSize and height > SmallSize:
    if width > height:
        height = int((SmallSize / width) * height)
        width = SmallSize
    else:
        width = int((SmallSize / height) * width)
        height = SmallSize

    print('Resizing %s...' % (filename))
    im = im.resize((width,height))

im.save(os.path.join('Thumbnail', filename))
