import os, random
IMG_PATH="Backgrounds/"
def RandomImage():
    img=random.choice(os.listdir(IMG_PATH))
    return IMG_PATH+img


