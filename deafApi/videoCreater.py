#libraries



import numpy as np
import cv2
import glob
import os
from moviepy.editor import *
#settings
from django.conf import settings

#models
from deafApi import models
from deafApi import text_processor

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

# def getVideoUsingAlphabets(ip):
#     alphabets = models.Alphabet.objects.all()
#     img_arr = []
#     # print(ip)
#     for letter in ip:
#         if letter == " ":
#             for _ in range(10):
#                 img_arr.append( np.zeros((HEIGHT, WIDTH, LAYERS)) )
#         else:
#             loc = imageFinder(alphabets,letter.capitalize() )
#             if loc:
#                 loc = loc[len(loc)-5::]
#                 # print(loc)
#                 loc1 = os.path.join( settings.MEDIA_ROOT, "Alphabet")
#                 loc = os.path.join( loc1, loc )
#                 # print(loc)
#                 img = cv2.imread(loc)
#                 for i in range(15):
#                     img_arr.append(img)
#         # print(len(img_arr))
#     # print(settings.MEDIA_ROOT)
#     op = settings.MEDIA_ROOT + "/Videos/" + ip + ".webm"
#     # out = cv2.VideoWriter(op, cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 25, SIZE) 
#     out = cv2.VideoWriter(op, cv2.VideoWriter_fourcc('V','P','8','0'), 25, SIZE)
#     for i in range(len(img_arr)):
#         out.write(img_arr[i])
#     out.release()
    
#     return "media/Videos/" + ip + ".webm"

#note Datatype of Alphabet Images - uint8 
#and frames are 15
def get_video_from_alphabet(input_word):
    # alphabets = models.Alphabet.objects.all()

    # Whole code here
    img_arr = []
    for char in input_word:
        
        if char.isalpha():
            charObj = models.Alphabet.objects.get( character = char.capitalize() )
            # print(charObj)
            path = settings.MEDIA_ROOT + '/' + str( charObj.data )
            img = cv2.imread( path )
            
            # append 15 frames into the array
            for i in range(15):
                img_arr.append( img )

        else:
            pass

    op = settings.MEDIA_ROOT + "/Videos/" + input_word + ".webm"
    save = cv2.VideoWriter(op, cv2.VideoWriter_fourcc('V','P','8','0'), 25, SIZE)
    
    for i in range(len(img_arr)):
        save.write(img_arr[i])
    save.release()


    clip = VideoFileClip(op) 
    return clip



def get_video_from_word(input_word):

    video_object = models.Word.objects.get(word=input_word)
    video_path = settings.MEDIA_ROOT  + '/' + str( video_object.data )
    clip = VideoFileClip(video_path)   
   
    # merged_video = concatenate_videoclips([clip1, clip2])
    # merged_video.write_videofile(settings.MEDIA_ROOT + '/Videos/' + "merged.webm")



def generateVideo(input_text, word_set):

    # text processing 
    processed_text = text_processor.process_text(input_text)
    processed_word_list = processed_text.split()

    clip_list = []
    
    for word in processed_word_list:
        
        if word in word_set:
            clip = get_video_from_word(word)
        
        else:
            clip = get_video_from_alphabet(word)
            
        clip_list.append(clip)

    merged_video = concatenate_videoclips(clip_list)
    merged_video.write_videofile(settings.MEDIA_ROOT + '/Videos/' + "merged.mp4")



if __name__ == '__main__':
    generateVideo("this ball Focus")

