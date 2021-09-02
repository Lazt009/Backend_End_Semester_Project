from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from deafApi import Serializers
from deafApi import models

from deafApi import videoCreater

# Create your views here.
@api_view(['GET'])
def alphabets(request):
    alphabet = models.Alphabet.objects.all()
    serializer = Serializers.AlphabetSerializer(alphabet, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def words(request):
    word = models.Word.objects.all()
    serializer = Serializers.WordSerializer(word, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def getVideo(request):
    print(request.data)
    if "text" in request.data.keys():
        #process text here
        processedText = request.data["text"]
        path = videoCreater.getVideoUsingAlphabets(processedText)
    return HttpResponse(path)