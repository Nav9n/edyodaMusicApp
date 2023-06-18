from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home1, name = "home1"),
    path('register',views.register, name = "register"),
    path('signin',views.signin, name = "signin"),
    path('upload',views.uploadPage, name = "uploadPage"),
    path('songs/', views.song_list, name='song_list'),
    path('upload/', views.upload_song, name='upload_song'),
    path('home/', views.home, name='home'),
     path('check-access/', views.check_access, name='check_access'),
    
    

      

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)