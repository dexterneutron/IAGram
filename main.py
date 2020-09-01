from IAgram import AddcenteredText,BrightnessFilter,IATransform,AddTransparentLayer
from PIL import Image,ImageFont,ImageFilter
from db import RamdomQuote
#variables for image size
size=612,612
#my quote
q,a=RamdomQuote()

sentence="{quote}. -{author}".format(quote=q,author=a)
i=Image.open("Backgrounds/background8.jpg")
i=i.resize(size)
img=IATransform('CenterWhiteBox',sentence,i)
#fnt = ImageFont.truetype('Fonts/CroissantOne-Regular.ttf', 50)
#img=AddcenteredText(sentence,i,fnt,textbox=True)
img.save('quote5.png')
