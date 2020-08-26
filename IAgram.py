from PIL import Image, ImageDraw,ImageFont,ImageFilter
BLUE=(6, 50,71)
BROWN=(112, 66, 20)
GREEN=(51,97,32)
PURPLE=(87,10,84)
GREYBLUE=(102,122,129)
YELLOW=(60,61,29)
LIGHTPURPLE=(41,0,62)
def IATransform(filter,sentence,i,color='none'):
    if filter=='DarkWhiteText':
        fnt = ImageFont.truetype('Fonts/CroissantOne-Regular.ttf', 50)
        brightness=0.3
        img=BrightnessFilter(i, brightness)
        img=AddcenteredText(sentence,img,fnt)
        return img
    elif filter=='ColourWhiteText':
        fnt = ImageFont.truetype('CroissantOne-Regular.ttf', 50)
        img=AddTransparentLayer(i,LIGHTPURPLE)
        img=AddcenteredText(sentence,img,fnt)
        return img
    else:
        print('Filter doesnt exist')

def AddcenteredText(sentence,img,fnt):
    d = ImageDraw.Draw(img)
    x1 = 612
    y1 = 612
    sum=0
    for letter in sentence:
        sum += d.textsize(letter, font=fnt)[0]
        average_length_of_letter = sum/len(sentence)
        #find the number of letters to be put on each line
        number_of_letters_for_each_line = (x1/1.618)/average_length_of_letter
        incrementer = 0
        fresh_sentence = ''
    #add some line breaks
    for letter in sentence:
        if(letter == '-'):
            fresh_sentence += '\n\n' + letter
        elif(incrementer < number_of_letters_for_each_line):
            fresh_sentence += letter
        else:
            if(letter == ' '):
                fresh_sentence += '\n'
                incrementer = 0
            else:
                fresh_sentence += letter
        incrementer+=1
    print (fresh_sentence)
    #render the text in the center of the box
    dim = d.textsize(fresh_sentence, font=fnt)
    x2 = dim[0]
    y2 = dim[1]
    qx = (x1/2 - x2/2)
    qy = (y1/2-y2/2)
    #d.text((qx-1, qy), fresh_sentence, align="center",font=fnt, fill=(0,0,0))
    #d.text((qx+1, qy), fresh_sentence,align="center", font=fnt, fill=(0,0,0))
    #d.text((qx, qy-1), fresh_sentence,align="center", font=fnt, fill=(0,0,0))
    #d.text((qx, qy+1), fresh_sentence,align="center", font=fnt, fill=(0,0,0))
    d.text((qx,qy), fresh_sentence ,align="center",  font=fnt, fill=(255,255,255))
    return img

def BrightnessFilter(i, br):
    img = Image.new('RGB', i.size)
    for x in range(i.size[0]):
        for y in range(i.size[1]):
            r, g, b = i.getpixel((x, y))
            red = int(r * br)
            red = min(255, max(0, red))
            green = int(g * br)
            green = min(255, max(0, green))
            blue = int(b * br)
            blue = min(255, max(0, blue))
            img.putpixel((x, y), (red, green, blue))
    return img

def AddTransparentLayer(i,color):
    front = Image.new('RGB', (612, 612), color = color)
    front.putalpha(100)
    i.paste(front,(0,0),mask=front)
    return i