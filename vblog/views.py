from django.shortcuts import render,redirect
from .views import *
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
def index(request):
    records=post.objects.all().order_by('-id')[1:]
    lastpost=post.objects.all().order_by('-id')[0]

    return render(request,"home.html",{"rec":records,"last":lastpost})
# Create your views here.

@login_required
def create_post(request):
    if request.method=="POST":
        form=postform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form=postform()

    return render(request,"post.html",{"form":form})
def detail(request,d):
    r=post.objects.get(id=d)
    return  render(request,"detail.html",{"s":r})

def delete(request,m):
    z=post.objects.get(id=m)
    z.delete()
    return redirect("index")

def back(request):
    return redirect("index")