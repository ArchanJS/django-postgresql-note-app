from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login,logout,authenticate
from pages.models import Post

# Create your views here.

#Home
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        posts=Post.objects.filter(postedBy=request.user)
        return render(request,"home.html",{
            "username":request.user.username,
            "posts":posts
        })

#Register
def register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        cpassword=request.POST.get("cpassword")
        if password!=cpassword:
            return redirect("/")
        else:
            user=User(username=username,password=make_password(password))
            user.save()
            return redirect("/login")
    else: 
        if not request.user.is_anonymous:
            return redirect("/")
        else:
            return render(request,"signup.html")
#Login
def loginFunc(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        login(request,user)
        return redirect("/")
    else:
        if not request.user.is_anonymous:
            return redirect("/")
        else:
            return render(request,"login.html")

#Logout
def logoutFunc(request):
    if not request.user.is_anonymous:
        logout(request)
        return redirect("/login")

#Create post
def createPost(request):
    if request.method=="POST":
        posttitle=request.POST.get("posttitle")
        content=request.POST.get("content")
        print(content)
        post=Post(postTitle=posttitle,postedBy=request.user,content=content)
        post.save()
    return redirect("/")

#Delete post
def deletePost(request,postId):
    Post.objects.filter(id=postId).delete()
    return redirect("/")

#Edit post
def editPost(request,postId):
    post=Post.objects.get(id=postId)
    return render(request,"edit.html",{
        "post":post
    })

#Update post
def updatePost(request,postId):
    if request.method=="POST":
        post=Post.objects.get(id=postId)
        post.postTitle=request.POST.get("posttitle")
        post.content=request.POST.get("content")
        post.save()
    return redirect("/")