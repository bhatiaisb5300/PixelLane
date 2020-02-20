from django.urls import path, include
from .views import index,images_view,get_exif
app_name = 'display'
urlpatterns = [
    path('',index,name='index'),
    path('boards/<genres>/',images_view,name='boards'),
    path('exif/',get_exif,name='exif'),
]
