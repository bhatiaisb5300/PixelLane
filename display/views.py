from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.conf import settings
from .models import images,board
from .exif import process_image
from pyzbar.pyzbar import decode
from PIL import Image
from base64 import b64encode
# Create your views here.


def index(request):
    return render(request,'index.html')

def images_view(request,genres):
    # print(genres.title())
    # def genre():
    #     return 'Wildlife'
    if request.method=="POST":
        if request.FILES['myfile']:
            inImg = request.FILES["myfile"].read()
            encoded = b64encode(inImg).decode('ascii')
            mime = "image/jpg"
            mime = mime + ";" if mime else ";"
            input_image = "data:%sbase64,%s" % (mime, encoded)
            try:
                decoded = decode(Image.open(request.FILES['myfile']))
            except:pass
            # print(input_image)
            print(decoded[0][0].decode())
            # obj = board.objects.get(genre=genres.title())
            # print(obj.detail1)
            # l=[1,2,3,4,5,6,7,8,9,10]
            # dict = {'item1':obj.detail1,'item2':obj.detail2,'item3':obj.detail3,'item4':obj.detail4,'item5':obj.detail5,'item6':obj.detail6,
            #         'item7':obj.detail7,'item8':obj.detail8,'item9':obj.detail9,'item10':obj.detail10,'genre':genres.title(),'image':input_image}
            return HttpResponseRedirect(decoded[0][0].decode())
    obj = board.objects.get(genre=genres.title())
    # print(obj.detail1)
    # l=[1,2,3,4,5,6,7,8,9,10]
    dict = {'item1':obj.detail1,'item2':obj.detail2,'item3':obj.detail3,'item4':obj.detail4,'item5':obj.detail5,'item6':obj.detail6,
            'item7':obj.detail7,'item8':obj.detail8,'item9':obj.detail9,'item10':obj.detail10,'genre':genres.title()}
    return render(request,'board.html',context=dict)





def get_exif(request):
    obj = images.objects.all()
    for item in obj:
        url = str(settings.BSE_ROOT) + str(item.image.url)
        tags = process_image(str(url))
        # print(tags)
        if 'Image Make' in tags           : item.brand = tags['Image Make']
        if 'Image Model' in tags          : item.model = tags['Image Model']
        if 'Image DateTime' in tags       : item.date = tags['Image DateTime']
        if 'EXIF ExposureTime' in tags    : item.shutterspeed = tags['EXIF ExposureTime']
        if 'EXIF FocalLength' in tags     : item.focallength = tags['EXIF FocalLength']
        if 'EXIF FNumber' in tags         : item.aperture = tags['EXIF FNumber']
        if 'EXIF ISOSpeedRatings' in tags : item.iso = tags['EXIF ISOSpeedRatings']
        if 'EXIF LensModel' in tags       : item.lens = tags['EXIF LensModel']
        item.save()
    return render(request,'index.html')
