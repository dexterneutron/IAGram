from IAgram import IATransform,RandomTransform
from PIL import Image,ImageFont
from imageLoader import RandomImage
from db import RamdomQuote,GetQuotesList
import time

OUTPUTPATH="Output/"
#variables for image size
size=612,612
#my quote
#q,a=RamdomQuote()
q=GetQuotesList()
index=0
start_time = time.time()
for q in q:
        f=(q['Frase'])
        a=(q['Autor'])
        sentence=f if a=="" else "{quote}. -{author}".format(quote=f,author=a)
        i=Image.open(RandomImage())
        i=i.resize(size)
        img=IATransform(RandomTransform(),sentence,i)
        imgpath="{path}image{i}.png".format(path=OUTPUTPATH,i=index)
        print(imgpath)
        img.save(imgpath)
        index+=1
print('All Images generated')
print('Execution Time: ')
print("--- %s seconds ---" % (time.time() - start_time))




#i=Image.open('Backgrounds/background24.jpg')

#img=IATransform('AlphaText',sentence,i)
#fnt = ImageFont.truetype('Fonts/CroissantOne-Regular.ttf', 50)
#img=AddcenteredText(sentence,i,fnt,textbox=True)
#img.save('quote5.png')
