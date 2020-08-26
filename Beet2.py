from IAgram import AddcenteredText,BrightnessFilter,IATransform,AddTransparentLayer
from PIL import Image,ImageFont,ImageFilter
#variables for image size
size=612,612
#my quote
sentence = "Some people want it to happen, some wish it would happen, others make it happen. -Michael Jordan"
i=Image.open("background2.jpg")
i=i.resize(size)
color = (6, 50, 71)
#fnt = ImageFont.truetype('CroissantOne-Regular.ttf', 50)
#i=AddcenteredText(sentence,i,fnt)
img=IATransform('ColourWhiteText',sentence,i)
#img=SepiaFilter(i)
img.save('quote4.png')
#color = (112, 66, 20)