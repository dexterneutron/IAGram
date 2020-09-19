import os, random
IMG_PATH="Backgrounds/"
def RandomImage():
    img=random.choice(os.listdir(IMG_PATH))
    return IMG_PATH+img

def ImagebyId(id):
    img="background{i}.jpg".format(i=id)
    return IMG_PATH+img
