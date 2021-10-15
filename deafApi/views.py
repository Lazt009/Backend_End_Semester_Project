from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import os

from django.conf import settings

from rest_framework.decorators import api_view
from rest_framework.response import Response

from deafApi import Serializers
from deafApi import models

from deafApi import videoCreater

from django.conf import settings


def fileDeleter():
    print( os.chdir( (settings.MEDIA_ROOT  + '\\Videos') ) )
    for files in os.listdir( (settings.MEDIA_ROOT  + '\\Videos') ):
        if files != '.buffer-file':
            os.remove(files)
    os.chdir( settings.MEDIA_ROOT )
    

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

    os.chdir()


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
        processedText = request.data["text"]
        path = videoCreater.getVideoUsingAlphabets(processedText)
    return HttpResponse(path)