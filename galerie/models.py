from django.db import models
import os
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
	email=models.EmailField(unique=True)
	pays=models.CharField(max_length=15)
	USERNAME_FIELD='email'
	REQUIRED_FIELDS=[]

	def __str__(self):
		return self.email
class save_image(models.Model):
	upload_time=models.DateTimeField(auto_now_add=True)
	picture=models.ImageField(upload_to='pictures/')

	def __str__(self):
		return self.picture

def user_upload_path(instance,filename):
         #folder = instance.folder
         #return folder
	#folder_name=instance.folder
	return os.path.join('folder_name',instance.folder.name,filename)

class Folder(models.Model):
	name=models.CharField(max_length=15,unique=True)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		return self.name

class UploadImage(models.Model):
    folder=models.CharField(max_length=20)
    image=models.FileField(upload_to=user_upload_path)
    def save(self,*args,**kwargs):
        if hasattr(self,'_custom_upload_to'):
           self.image.field.upload_to = self._custom_upload_to
           super(UploadImage,self).save(*args,**kwargs)
    def __str__(self):
       return self.folder


class Abc(models.Model):
   data = models.TextField()
class Corbeille(models.Model):
      user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
      folder = models.ForeignKey(Folder,on_delete=models.CASCADE,null=True)
      img=models.FileField(upload_to='corbeille/')



