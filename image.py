import os
from PIL import Image

def add_watermark(photo_infile):
    photo = Image.open(photo_infile)
    watermark = Image.open("images/watermark_white.png")

    watermark_height, watermark_width = watermark.height, watermark.width
    new_watermark_height = photo.height/3

    watermark = watermark.resize(((int(new_watermark_height), int((watermark_height/watermark_width)*new_watermark_height))))
    watermark.convert("RGBA")

    position = ((photo.width - watermark.width), (photo.height - watermark.height))

    photo.paste(watermark, position, watermark)

    return photo

def process_photo(photo_infile, photo_outfile, photo_size, thumb_size):
    watermarked = add_watermark(photo_infile)
    thumb = watermarked.copy()
    
    watermarked.thumbnail((photo_size, photo_size))
    watermarked.save(photo_outfile)
    print(photo_outfile)

    thumb.thumbnail((thumb_size, thumb_size))
    thumb_outfile = photo_outfile.split(".jpg")[0] + "_thumb.jpg"
    thumb.save(thumb_outfile)
    print(thumb_outfile)

def process_folder(sizes):
    for s in sizes:
        folder_size, photo_size, thumb_size = s
        base_folder = "images/full_nt/"
        filenames = os.listdir(base_folder)
        for i in filenames:
            process_photo(base_folder+i, "static/images/"+ folder_size + "/" + i, photo_size, thumb_size)

sizes = [("high", 750, 500), ("med", 500, 300)]

process_folder(sizes)



