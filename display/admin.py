from django.contrib import admin

# Register your models here.
from .models import images,board

admin.site.register(images)
admin.site.register(board)
# admin.site.register(image)
