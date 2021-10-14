#libraries
import numpy as np
import cv2
import glob
import os

#settings
from django.conf import settings

#models
from deafApi import models

#global Constants
HEIGHT, WIDTH, LAYERS =  1080, 1440, 3
SIZE = (WIDTH, HEIGHT)

def imageFinder(alphabets, letter):
    for alphabet in alphabets:
        # print(alphabet.title, alphabet.image)
        if letter == alphabet.character:
            return str(alphabet.data)
    else:
        return False

def getVideoUsingAlphabets(ip):
    alphabets = models.Alphabet.objects.all()
    img_arr = []
    # print(ip)
    for letter in ip:
        if letter == " ":
            for _ in range(10):
                img_arr.append( np.zeros((HEIGHT, WIDTH, LAYERS)) )
        else:
            loc = imageFinder(alphabets,letter.capitalize() )
            if loc:
                loc = loc[len(loc)-5::]
                # print(loc)
                loc1 = os.path.join( settings.MEDIA_ROOT, "Alphabet")
                loc = os.path.join( loc1, loc )
                # print(loc)
                img = cv2.imread(loc)
                for i in range(15):
                    img_arr.append(img)
        # print(len(img_arr))
    # print(settings.MEDIA_ROOT)
    op = settings.MEDIA_ROOT + "/Videos/" + ip + ".webm"
    # out = cv2.VideoWriter(op, cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 25, SIZE) 
    out = cv2.VideoWriter(op, cv2.VideoWriter_fourcc('V','P','8','0'), 25, SIZE)
    for i in range(len(img_arr)):
        out.write(img_arr[i])
    out.release()
    
    return "media/Videos/" + ip + ".webm"