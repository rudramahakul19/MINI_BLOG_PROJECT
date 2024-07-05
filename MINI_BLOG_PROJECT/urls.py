"""MINI_BLOG_PROJECT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.HOME),
    path("about/",views.ABOUT,name='about'),
    path("contact/",views.CONTACT,name='contact'),
    path("dashboard/",views.DASHBOARD,name='dashboard'),
    path("signup/",views.SIGN_UP,name='user_signup'),
    path("login/",views.USER_LOGIN,name='user_login'),
    path("logout/",views.USER_LOGOUT,name='user_logout'),
    path("addpost/",views.ADD_POST,name='add_post'),
    path("updatepost/<int:id>/",views.UPDATE_POST,name='update_post'),
    path("deletepost/<int:id>/",views.DELETE_POST,name='delete_post'),


]
