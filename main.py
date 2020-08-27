from IAgram import AddcenteredText,BrightnessFilter,IATransform,AddTransparentLayer
from PIL import Image,ImageFont,ImageFilter
#variables for image size
size=612,612
#my quote
sentence = "Some people want it to happen, some wish it would happen, others make it happen. -Michael Jordan"
i=Image.open("Backgrounds/background6.jpg")
i=i.resize(size)
img=IATransform('CenterWhiteBox',sentence,i)        
#fnt = ImageFont.truetype('Fonts/CroissantOne-Regular.ttf', 50)
#img=AddcenteredText(sentence,i,fnt,textbox=True)
img.save('quote5.png')
