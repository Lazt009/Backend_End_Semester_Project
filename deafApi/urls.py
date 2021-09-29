from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

# Importing Views
from deafApi import views

urlpatterns = [
    path('', views.default, name="Default"),
    path('alphabet/', views.alphabets, name='Alphabet'),
    path('word/', views.words, name="Word"),
    path('get-video/', views.getVideo, name="Get-Video"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)