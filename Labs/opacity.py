from PIL import Image, ImageDraw, ImageFont
from imageLoader import RandomImage
size=612,612

# get an image
base = Image.open(RandomImage()).resize(size)

# make a blank image for the text, initialized to transparent text color
txt = Image.new('L',size, (0))

# get a font
fnt = ImageFont.truetype('Fonts/Philosopher-Bold.ttf', 40)
# get a drawing context
d = ImageDraw.Draw(txt)

# draw text, half opacity
#d.text((10,10), "Hello", font=fnt, fill=(255,255,255,128))
# draw text, full opacity
d.text((10,60), "Do one thing every day that scares you", font=fnt, fill=(255))
baserbg=base.copy()
baserbg.putalpha(txt)
#txt.convert('L').resize(im_rgb.size)
#out = Image.alpha_composite(base, txt)

#out.show()
baserbg.show()