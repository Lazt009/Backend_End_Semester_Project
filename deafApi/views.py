from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import os
import cv2
from moviepy.editor import *

from django.conf import settings

from rest_framework.decorators import api_view
from rest_framework.response import Response

from deafApi import Serializers
from deafApi import models

from deafApi import videoCreater

from django.conf import settings

#global Constants
HEIGHT, WIDTH, LAYERS =  1080, 1440, 3
SIZE = (WIDTH, HEIGHT)


def fileDeleter():
    media = os.path.join( settings.MEDIA_ROOT, "Videos" )

    for videos in os.listdir(media):
        if videos != '.buffer-file':
            print((settings.MEDIA_ROOT + '/Videos/' + videos))
            os.remove( (settings.MEDIA_ROOT + '/Videos/' + videos) )
            
    

# Create your views here.
def default(request):
    # cwd = os.getcwd()
    media = os.path.join( settings.MEDIA_ROOT, "Videos" )
    # print(media)/
    D = {}
    for videos in os.listdir(media):
        if videos.endswith('.webm'):
            D[ videos ] = "path"
    return render(request, "deafApi/DefaultPage.html", {"Data" : D})


@api_view(['GET'])
def alphabets(request):
    # Deleting the files which was present prior to this api call
    fileDeleter()

    alphabet = models.Alphabet.objects.all()
    serializer = Serializers.AlphabetSerializer(alphabet, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def words(request):
    # Deleting the files which was present prior to this api call
    fileDeleter()

    # word = models.Word.objects.all()
    # word_set = set()
    # for i in word:            
    #     print(i.word)
    #     word_set.add( i.word.lower() )
    # print("\n\n\n", word_set)


    # path = videoCreater.generateVideo("Focus now", word_set)

    # focusobj = models.Word.objects.get(word='Focus')
    # path1 = settings.MEDIA_ROOT  + '/' + str( focusobj.data )
    # accountobj = models.Word.objects.get(word='Account')
    # path2 = settings.MEDIA_ROOT + '/' + str( accountobj.data )

    # # print("\n\n path1", path1)

    # clip1 = VideoFileClip(path1)   
    # clip2 = VideoFileClip(path2) 

    # merged_video = concatenate_videoclips([clip1, clip2])
    # merged_video.write_videofile(settings.MEDIA_ROOT + '/Videos/' + "merged.webm")

    # merged_video.ipython_display(width = 480)

    
    # # Check if camera opened successfully
    # if (cap.isOpened()== False):
    #     print("Error opening video stream or file")
    # # Read until video is completed
    # while(cap.isOpened()):
    #     # Capture frame-by-frame
    #     ret, frame = cap.read()
    #     print(frame)
    #     if ret == True:
    #         # Display the resulting frame
    #         cv2.imshow('Frame',frame)
    #         # Press Q on keyboard to  exit
    #         if cv2.waitKey(25) & 0xFF == ord('q'):
    #             break
    #     # Break the loop
    #     else:
    #         break
    # # When everything done, release the video capture object
    # cap.release()


    word = models.Word.objects.all()
    serializer = Serializers.WordSerializer(word, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def getVideo(request):
    print(request.data)
    # Deleting the files which was present prior to this api call
    fileDeleter()

    if "text" in request.data.keys():
        #process text here
        text = request.data["text"]

        word = models.Word.objects.all()
        word_set = set()
        for i in word:
            print(i.word)
            word_set.add(i.word)
        print("\n\n\n", word_set)

        path = videoCreater.generateVideo(text, word_set)
    return HttpResponse(path)