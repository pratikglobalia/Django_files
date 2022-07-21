from django.shortcuts import render
from .models import Page, Post, Song, User

# Create your views here.
def home(request):
    return render(request, 'home.html')

def show_pagedata(request):
    data = Page.objects.all()
    return render(request, 'page.html', {'data':data})
    
def show_postdata(request):
    data = Post.objects.all()
    return render(request, 'post.html', {'data':data})
    
def show_songdata(request):
    data = Song.objects.all()
    return render(request, 'song.html', {'data':data})
    
def show_userdata(request):
    data = User.objects.all()
    return render(request, 'user.html', {'data':data})
    