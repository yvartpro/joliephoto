import os
from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Folder,UploadImage,Corbeille
# Create your views here.
User=get_user_model()
def signin(request):
	if request.method=='POST':
		email=request.POST.get('email')
		password=request.POST.get('password')

		user=authenticate(email=email,password=password)
		if user is not None:
			login(request,user)
			return redirect('home')
		else:
			context = {
				"sapor":"user is not None"
			}
		return render(request,'galerie/login.html',context)
	return render(request,'galerie/login.html')
def register(request):
	if request.method=='POST':
		email=request.POST.get('email')
		pays=request.POST.get('pays')
		password=request.POST.get('password')
		password2=request.POST.get('password2')
		print(password2)
		try:
			member = User.objects.get(email=email)
			if member:
				context = {
					"sapor":"user is alredy in the system"
				}
				return render(request,'galerie/inscrire.html',context)
		except:
			print('new member')

		if password != password2:
			context = {
				"sapor":"password not the same"
			}
			return render(request,'galerie/inscrire.html',context)
		else:
			user=User.objects.create_user(username=email,email=email,password=password)
			user.pays=pays
			user.save()
			return redirect('signin')
	return render(request,'galerie/inscrire.html')
@login_required
def home(request):
    try:
       folders = Folder.objects.filter(user=request.user)
       context =  {
         'folders':folders,
       }
       return render(request,'galerie/index.html',context)
    except Exception as e:
         print(e)
    return render(request,'galerie/index.html')
def folder(request):
	if request.method == 'POST':
		name=request.POST.get('folder')
		print(name)
		path="/home/buffalo/project/georgete/joliephoto/media/"
		folder= path + name
		os.makedirs(folder,exist_ok=True)
		try:
			folder = Folder.objects.get(name=name)
			if folder:
				context = {
        			'sapor':'folder exist'
				}
				print('file exist')
				return redirect('home')
		except:
			print('not exist')
			folder=Folder(name=name,user=request.user)
			folder.save()

	return redirect('home')
def gallery(request):
	folder=Folder.objects.all()
	context={
	"folder":folder
}
	return render(request,'galerie/gallery.html',context)

def folder_files(request,folder_id):
	folder=Folder.objects.get(id=folder_id)
	context={
	"folder":folder
	}
	return render(request,'galerie/folder_files.html',context)

def uploadimage(request):
	if request.method=="POST":
		folder=request.POST.get("folder")
		image=request.FILES.get("image")
		print(folder)
		print(image)
		last_id=UploadImage.objects.order_by('id').last()
		if last_id:
			new_id=last_id.id+1
		else:
			new_id=1

		#folder=Folder.objects.get(name=folder)
		#new=UploadImage(folder=folder,image=image)
		relative_folder_path = os.path.join(folder)
		new= UploadImage()
		#new._custom_upload_to = os.path.join(settings.MEDIA_ROOT,folder)
		new._custom_upload_to = relative_folder_path
		new.folder = folder
		new.image =image
		new.save()
		return redirect('home')
@login_required
def image(request,image_id):
	folder=Folder.objects.get(id=image_id)
	print(folder)
	photo=UploadImage.objects.filter(folder=folder)
	print(photo)
	context = {
		"folder":folder,
                "photo":photo,
	}
	return render(request,'galerie/image.html',context)
def delete_image(request,image_id):
    img=UploadImage.objects.get(id=image_id)
    folder=img.folder
    folder = Folder.objects.get(name=folder)
    corb=Corbeille(user=request.user,folder=folder,img=img.image)
    corb.save()
    img.delete()
    return redirect('home')
def corbeille(request):
    img = Corbeille.objects.filter(user=request.user)
    context = {
      'img':img
    }
    return render(request,'galerie/corbeille.html',context)
def signout(request):
    logout(request)
    return redirect('signin')

def delete_old(request,image_id):
    img=Corbeille.objects.get(id=image_id)
    img.delete()
    return redirect('corbeille')
def restore(request,image_id):
    img=Corbeille.objects.get(id=image_id)
    folder = img.folder
    image = img.img
    folders = Folder.objects.get(name=folder)
    f = str(folder)
    print(f)
    relative_folder_path = os.path.join(f)
    new = UploadImage()
    new._custom_upload_to = relative_folder_path
    new.folder = f
    new.image = image
    new.save()
    img.delete()
    return redirect('home')
