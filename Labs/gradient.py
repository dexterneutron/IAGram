from PIL import Image, ImageFont, ImageDraw

OUTPUT_IMAGE = '53952270.png'
BG_COLOR = (0, 102, 0)
TEXT = 'STIEFELSTANGE'
TEXT_COLOR = (255, 255, 255)
#SHADOW_COLOR(51,97,32)
SHADOW_COLOR = (231, 255, 227)

image = Image.new('RGB', (212, 45), color=BG_COLOR)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('impact', 36)
text_size = font.getsize(TEXT)
draw.text((0, 0), TEXT, font=font)
pixels = image.load()
size = image.size

x_list = []
y_list = []
for x in range(size[0]):
    for y in range(size[1]):
        if pixels[x, y] == TEXT_COLOR:
            x_list.append(x)
            y_list.append(y)

shadow_height = text_size[1]/4
for x, y in zip(x_list, y_list):
    if y < min(y_list) + shadow_height or y > max(y_list)-shadow_height:
        pixels[x, y] = SHADOW_COLOR

image.save(OUTPUT_IMAGE)