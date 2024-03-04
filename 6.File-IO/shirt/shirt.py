import os, sys
from PIL import Image, ImageOps

if len(sys.argv) == 3:
    formats = [".jpg", ".jpeg", ".png"]
    ext1 = os.path.splitext(sys.argv[1])
    ext2 = os.path.splitext(sys.argv[2])
    if ext1[1] == ext2[1] and ext1[1] in formats:
        try:
            with Image.open(sys.argv[1]) as imfile:
                shirt = Image.open("shirt.png")
                size = shirt.size
                imshirt = ImageOps.fit(imfile, size)
                imshirt.paste(shirt, shirt)
                imshirt.save(sys.argv[2])
        except FileNotFoundError:
            sys.exit("File does not exist")
    elif ext1[1] != ext2[1]:
        sys.exit("Input and output have different extensions")
    else:
        sys.exit("Invalid output")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")