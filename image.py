import os
from PIL import Image

def add_watermark(photo_infile):
    photo = Image.open(photo_infile)
    thumb = photo.copy()
    watermark = Image.open("images/watermark.png")

    watermark_height, watermark_width = watermark.height, watermark.width
    new_watermark_height = photo.height/2

    watermark = watermark.resize(((int(new_watermark_height), int((watermark_height/watermark_width)*new_watermark_height))))
    watermark.convert("RGBA")

    position = ((int(photo.width/2) - int(watermark.width/2)), int(photo.height*(2/3)))

    photo.paste(watermark, position, watermark)

    return photo, thumb

def process_photo(photo_infile, photo_outfile, photo_size, thumb_size):
    watermarked, thumb = add_watermark(photo_infile)
    
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
        base_folder = "images/full/"
        filenames = os.listdir(base_folder)
        for i in filenames:
            process_photo(base_folder+i, "static/images/"+ folder_size + "/" + i, photo_size, thumb_size)

sizes = [("high", 750, 500), ("med", 500, 300), ("low", 350, 200)]

process_folder(sizes)



