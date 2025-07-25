from django.contrib import admin
from .models import User,Folder,UploadImage,Corbeille
# Register your models here.
admin.site.register(User)
admin.site.register(Folder)
admin.site.register(UploadImage)
admin.site.register(Corbeille)
