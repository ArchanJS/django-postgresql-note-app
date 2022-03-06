from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path("",views.index,name="homepage"),
    path("signup",views.register,name="registerpage"),
    path("login",views.loginFunc,name="loginpage"),
    path("logout",views.logoutFunc,name="logoutpage"),
    path("createpost",views.createPost,name="createnote"),
    path("delete/<str:postId>",views.deletePost,name="deletenote"),
    path("edit/<str:postId>",views.editPost,name="editnote"),
    path("update/<str:postId>",views.updatePost,name="updatepost")
]