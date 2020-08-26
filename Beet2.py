from IAgram import AddcenteredText,BrightnessFilter,IATransform,AddTransparentLayer
from PIL import Image,ImageFont,ImageFilter
#variables for image size
size=612,612
#my quote
sentence = "Some people want it to happen, some wish it would happen, others make it happen. -Michael Jordan"
i=Image.open("Backgrounds/background2.jpg")
i=i.resize(size)
img=IATransform('ColourWhiteText',sentence,i)
img.save('quote4.png')
