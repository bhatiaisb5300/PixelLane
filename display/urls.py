from django.urls import path, include
from .views import index,wildlife_view,get_exif,qr
urlpatterns = [
    path('',index,name='index'),
    path('boards/<genres>/',wildlife_view,name='Wildlife'),
    path('exif/',get_exif,name='exif'),
    path('qr/',qr,name='qr'),
]
