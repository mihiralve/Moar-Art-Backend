import os
from PIL import Image

def add_watermark(photo_infile, photo_outfile):
    photo = Image.open(photo_infile)
    watermark = Image.open("images/watermark_white.png")

    watermark_height, watermark_width = watermark.height, watermark.width
    new_watermark_height = photo.height/3

    watermark = watermark.resize(((int(new_watermark_height), int((watermark_height/watermark_width)*new_watermark_height))))
    watermark.convert("RGBA")

    position = ((photo.width - watermark.width), (photo.height - watermark.height))

    photo.paste(watermark, position, watermark)

    photo.save(photo_outfile)

def process_folder(folder):
    filenames = os.listdir(folder)
    for i in filenames:
        print(folder+i)
        add_watermark(folder+i, "static/"+ folder + i)

process_folder("images/high/")



