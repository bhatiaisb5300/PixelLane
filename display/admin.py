from django.contrib import admin

# Register your models here.
from .models import wildlife,board

admin.site.register(wildlife)
admin.site.register(board)
# admin.site.register(image)
