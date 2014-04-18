from PIL import Image, ImageFont, ImageDraw
import random


for item in range(0, 10):
    dumpedImage = Image.new("RGB", (1800, 30))
    
    drawImage = ImageDraw.Draw(dumpedImage)
    
    glyphStreamLength = 16
    
    text = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%^&*();,.<>?:"[]\{}|_-+=~'
    shuffledText = ''.join(random.sample(text, len(text)))[:glyphStreamLength] 
    
    fontToDraw = ImageFont.truetype("matrix_code.ttf", 30)
    
    location = 0, 0
    for glyph in shuffledText:
        # 00FFFF - ice blue
        # 00FF00 - green
        drawImage.text(location, glyph, font = fontToDraw, fill = '#00FF00')
        location = location[0] + 20, location[1]
    
    #4 tuple left upper right lower
    box = dumpedImage.getbbox()
    newbox = box[0] - 2, box[1] - 2, box[2] + 2, box[3] + 2
    
    dumpedImage = dumpedImage.crop(newbox)
    
    dumpedImage.save("green-image" + str(item) + ".png")