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

from deafApi import constants

# def imageFinder(alphabets, letter):
#     for alphabet in alphabets:
#         # print(alphabet.title, alphabet.image)
#         if letter == alphabet.character:
#             return str(alphabet.data)
#     else:
#         return False

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

# def get_video_from_alphabet1(input_word):
#     image_list = []

#     for letter in input_word:
#         if(letter.isalpha() or letter.isnum()):
#             charObj = models.Alphabet.objects.get( character = letter.capitalize() )
#             # print(charObj)
#             path = settings.MEDIA_ROOT + '/' + str( charObj.data )
#             image_list.append(path)
#         else:
#             pass

#     clip = ImageSequenceClip(image_list, fps=25)
#     return clip

def get_video_from_alphabet(input_word):
    clip_arr = []
    for j, char in enumerate(input_word):
        if char.isalpha():
            charObj = models.Alphabet.objects.get( character = char.capitalize() )
            path = settings.MEDIA_ROOT + "/" + str( charObj.data )
            print("\n\n\nPath - {}\n\n".format(path))
            clip = VideoFileClip(path)
            clip = clip.fx( vfx.speedx, 2.5)
            clip_arr.append(clip)
    merged_clip = concatenate_videoclips(clip_arr)
    # path = settings.MEDIA_ROOT + "/Videos/" + input_word + ".mp4"
    # merged_clip.write_videofile( path )

    # clip = VideoFileClip(path)   
    return merged_clip 

# def get_video_from_alphabet(input_word):
#     # alphabets = models.Alphabet.objects.all()

#     # Whole code here
#     img_arr = []
#     for j, char in enumerate(input_word):
#         if j>0 and input_word[j-1] == char:
#             black_screen = cv2.imread(settings.MEDIA_ROOT + '/Alphabet/Black.jpg')
#             black_screen = cv2.resize(black_screen, (1280, 720) )
#             for i in range( constants.BLACK_FRAME_FOR_SAME_LETTERS ):
#                 img_arr.append(black_screen)
#         if char.isalpha():
#             charObj = models.Alphabet.objects.get( character = char.capitalize() )
#             # print(charObj)
#             path = settings.MEDIA_ROOT + '/' + str( charObj.data )
#             img = cv2.imread( path )
#             img = cv2.resize(img, constants.SIZE )
#             # append 15 frames into the array
#             for i in range( constants.IMAGE_FRAMES ):
#                 img_arr.append( img )
#         else:
#             pass
     
#     black_screen = cv2.imread(settings.MEDIA_ROOT + '/Alphabet/Black.jpg')
#     black_screen = cv2.resize(black_screen, constants.SIZE )
#     for i in range( constants.BLACK_FRAME ):
#         img_arr.append(black_screen)

#     op = settings.MEDIA_ROOT + "/Videos/" + input_word + ".mp4"
#     # save = cv2.VideoWriter(op, cv2.VideoWriter_fourcc('V','P','8','0'), 25, SIZE)
#     save = cv2.VideoWriter(op, cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), constants.FPS, constants.SIZE ) 
#     for i in range(len(img_arr)):
#         save.write(img_arr[i])
#     save.release()

#     # clip = ImageSequenceClip(img_arr, fps=25)
#     clip = VideoFileClip(op) 
#     return clip



def get_video_from_word(input_word):

    video_object = models.Word.objects.get(word=input_word)
    print("\n\n\n Video_Object ",video_object,"\n\n")
    video_path = settings.MEDIA_ROOT  + '/' + str( video_object.data )
    print("\n\n\n Video path - ", video_path, "\n\n")
    clip = VideoFileClip(video_path)   
    return clip
   
    # merged_video = concatenate_videoclips([clip1, clip2])
    # merged_video.write_videofile(settings.MEDIA_ROOT + '/Videos/' + "merged.webm")


def isDigit(word):
    digit = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    if word in digit:
        ind = digit.index(word)
        return ind+1, True
    else:
        return -1, False


def checkSize(clip):
    wd, ht = clip.size
    width_ratio = constants.WIDTH / wd
    height_ratio = constants.HEIGHT / ht
    if width_ratio == 1 and height_ratio == 1:
        return clip
    elif width_ratio == height_ratio:
        clip = clip.resize( width_ratio )
    else:
        clip = clip.resize( max(width_ratio, height_ratio) )
    return clip   


def generateVideo(input_text, word_set):

    # text processing 
    processed_text = text_processor.process_text(input_text)
    processed_word_list = processed_text.split()

    clip_list = []
    
    for word in processed_word_list:
        num, flag = isDigit(word)
        if (word in word_set):
            clip = get_video_from_word(word)
        elif flag:
            clip = get_video_from_word( str(num) )
        else:
            clip = get_video_from_alphabet(word)
        # print(clip)
        
        # temp = cv2.imread(settings.MEDIA_ROOT + '/Alphabet/Black.jpg')
        clip = checkSize(clip)
        clip_list.append(clip)

    merged_video = concatenate_videoclips(clip_list)
    output = settings.MEDIA_ROOT + '/Videos/' + "merged.mp4"
    merged_video.write_videofile( output )
    
    return '/media/Videos/merged.mp4'


if __name__ == '__main__':
    generateVideo("this ball Focus")

