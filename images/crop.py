import os
from PIL import Image

directory = "C:/Users/junwe/Documents/FFXIV-Elemental-Raid-Macros/images/ultimates"

for path, folders, files in os.walk(directory):
    for f in files:
        if f.endswith(".jpg"):
            img = Image.open(os.path.join(path, f))
            imgWidth, imgHeight = img.size

            if imgWidth == imgHeight + 1 and imgHeight in [500, 1000]:
                left = 0
                top = 0
                width = imgHeight
                height = imgHeight

                box = (left, top, left + width, top + height)

                print("Cropping " + f)

                area = img.crop(box)
                area.save(os.path.join(path, f), 'jpeg')
