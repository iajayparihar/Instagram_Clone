from django.shortcuts import render,redirect
from .models import Post,Comment

# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required
def index(request):
    return render(request,'index.html')

def upload(request):
    if request.method == 'POST':
        upload_pic = request.POST.get('pic')
        upload_cap = request.POST.get('cap')
#===============pending============

        return render(request,"upload/upload.html",{'image':"data is saved."})
    print('i am in get ')
    return render(request,'upload/upload.html')

def chat(request):
    return render(request,'chat/chat.html')

def profile(request):
    allpost = Post.objects.all()
    print(allpost)
    return render(request,"profile/profile.html",{'allpost':allpost})

def reels(request):
    return render(request,'reels/reels.html')

#here we can save over file to database / redirect to same page again
def file_upload(request):
    return render(request,"upload/upload.html")
