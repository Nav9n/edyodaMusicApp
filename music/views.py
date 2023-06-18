
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login
from .forms import UploadSongForm
from .models import Song
from django.contrib.auth.decorators import login_required



def home1(request):
    return render(request, "authentication/index.html")

def register(request):
      
      if request.method == "POST":
         username = request.POST['username']
         email = request.POST['email']
         password= request.POST['pass']

         myuser = User.objects.create_user(username, email, password)

         myuser.save()
           
         messages.success(request,"you are registered with edYoda music platform.")

         

      return render(request, "authentication/register.html")

def signin(request):
    if request.method == "POST":
        username1 =  request.POST['username']
        pass1 = request.POST['pass']
        user = authenticate(username=username1, password=pass1)
        if user is not None:
            login(request, user)
            return redirect(upload_song)
        else:
            messages.error(request, "incorrect details!")
            return redirect(home1)
            

    return render(request, "authentication/signin.html")

def uploadPage(request):
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    
        
    return render(request, "authentication/uploadPage.html")

@login_required
def upload_song(request):
    if request.method == 'POST':
        form = UploadSongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.uploaded_by = request.user
            song.save()
            form.save_m2m()  # Save the many-to-many relationships
            
            return redirect('home')
    else:
        form = UploadSongForm()
    
    return render(request, 'upload.html', {'form': form})


def song_list(request):
    songs = Song.objects.all()
    return render(request, 'song_list.html', {'songs': songs})

@login_required
def home(request):
    user_email = request.user.email
    
    public_songs = Song.objects.filter(privacy_access='public')
    private_songs = Song.objects.filter(uploaded_by=request.user)
    protected_songs = Song.objects.filter(allowed_emails=request.user)
    
    songs = public_songs | private_songs | protected_songs
    
    return render(request, 'check access.html', {'songs': songs})

def check_access(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            accessible_songs = Song.objects.filter(allowed_emails=user)
            return render(request, 'access.html', {'accessible_songs': accessible_songs})
    
    return redirect('home')