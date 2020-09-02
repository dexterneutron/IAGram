from IAgram import AddcenteredText,BrightnessFilter,IATransform,AddTransparentLayer,RandomTransform
from PIL import Image,ImageFont,ImageFilter
from imageLoader import RandomImage
from db import RamdomQuote

#variables for image size
size=612,612
#my quote
q,a=RamdomQuote()

sentence="{quote}. -{author}".format(quote=q,author=a)
i=Image.open(RandomImage())
i=i.resize(size)
#img=IATransform(RandomTransform(),sentence,i)
img=IATransform('AlphaText',sentence,i)
#fnt = ImageFont.truetype('Fonts/CroissantOne-Regular.ttf', 50)
#img=AddcenteredText(sentence,i,fnt,textbox=True)
img.save('quote5.png')
