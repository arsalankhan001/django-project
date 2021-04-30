from django.contrib import admin
from django.urls import path,include
from home import views
admin.site.site_header = "arsalan khan site"
admin.site.site_title = "arsalan khan "
admin.site.index_title  = "arsalan khan site admin"



urlpatterns = [
    path("",views.index,name='home'),
    path("login",views.loginuser, name='login'),
    path("signup",views.signup, name='signup'),
    path("devinfo",views.devinfo, name='devinfo'),
    path("addinfo",views.addinfo, name='addinfo'),
    path("logout",views.logoutUser, name='logout'),
    path("search",views.search, name='search')

    
   
]
