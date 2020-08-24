from PIL import Image, ImageDraw,ImageFont,ImageFilter
#variables for image size
x1 = 612
y1 = 612
size=612,612
#my quote
sentence = "Some people want it to happen, some wish it would happen, others make it happen. -Michael Jordan"
fnt = ImageFont.truetype('CroissantOne-Regular.ttf', 50)

#img = Image.new('RGB', (x1, y1), color = (255, 255, 255))
img=Image.open("background.jpg")
img=img.resize(size)
#img = img.filter(ImageFilter.BoxBlur(2))
img.putalpha(128)
d = ImageDraw.Draw(img)
#find the average size of the letter
sum = 0
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
d.text((qx-1, qy), fresh_sentence, align="center",font=fnt, fill=(0,0,0))
d.text((qx+1, qy), fresh_sentence,align="center", font=fnt, fill=(0,0,0))
d.text((qx, qy-1), fresh_sentence,align="center", font=fnt, fill=(0,0,0))
d.text((qx, qy+1), fresh_sentence,align="center", font=fnt, fill=(0,0,0))
d.text((qx,qy), fresh_sentence ,align="center",  font=fnt, fill=(255,255,255))

img.save('quote1.png')