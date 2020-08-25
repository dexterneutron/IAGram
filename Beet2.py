from IAgram import AddcenteredText,BrightnessFilter,IATransform
from PIL import Image,ImageFont,ImageFilter
#variables for image size
size=612,612
#my quote
sentence = "Some people want it to happen, some wish it would happen, others make it happen. -Michael Jordan"
i=Image.open("background3.jpg")
i=i.resize(size)
brightness=0.3
img=IATransform('WhiteText',sentence,i)
img.save('quote.png')