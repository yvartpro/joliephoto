from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('',views.signin,name="signin"),
	path('signin',views.signin,name="signin"),
	path('register',views.register,name="register"),
	path('home',views.home,name="home"),
	path('folder',views.folder,name="folder"),
	path('image/<int:image_id>',views.image,name="image"),
	path('uploadimage',views.uploadimage,name="uploadimage"),
        path('delete_image/<int:image_id>',views.delete_image,name="delete_image"),
        path('corbeille',views.corbeille,name='corbeille'),
        path('signout',views.signout,name='signout'),
        path('delete_old/<int:image_id>',views.delete_old,name='delete_old'),
        path('restore<int:image_id>',views.restore,name='restore'),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
