from PIL import Image, ImageDraw, ImageFont

def add_watermark(photo_infile):
    photo = Image.open(photo_infile)
    watermark = Image.open("./watermark_white.png")

    watermark_height, watermark_width = watermark.height, watermark.width
    new_watermark_height = photo.height/3

    watermark = watermark.resize(((int(new_watermark_height), int((watermark_height/watermark_width)*new_watermark_height))))
    watermark.convert("RGBA")

    position = ((photo.width - watermark.width), (photo.height - watermark.height))

    photo.paste(watermark, position, watermark)

    photo.show()

add_watermark("./full/blauet.jpg")
