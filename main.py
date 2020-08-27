from IAgram import AddcenteredText,BrightnessFilter,IATransform,AddTransparentLayer,AddTextBox
from PIL import Image,ImageFont,ImageFilter
#variables for image size
size=612,612
#my quote
sentence = "Some people want it to happen, some wish it would happen, others make it happen. -Michael Jordan"
i=Image.open("Backgrounds/background4.jpg")
i=i.resize(size)
#img=IATransform('ColourWhiteText',sentence,i)
img=AddTextBox(i)
img.save('quote5.png')
