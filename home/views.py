from django.shortcuts import render
from home.models import Addinfo
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, logout,login
# Create your views here.

def loginuser(request):
     if request.method == "POST":
          username = request.POST.get('username')
          password = request.POST.get('password')
          user = authenticate(username=username,password=password)
          if user is not None:
               login(request,user)
               return redirect("/")
          else:
               return render(request,'login.html')
          

     return render(request,'login.html')
def signup(request):
     return render(request,'signup.html')  
def devinfo(request):
     return render(request,'devinfo.html')
def addinfo(request):
     if request.method == "POST":
          name = request.POST.get('name')
          email = request.POST.get('email')
          tech = request.POST.get('tech')
          loc1 = request.POST.get('loc1')
          domain = request.POST.get('domain')
          proj = request.POST.get('proj')
          blo1 = request.POST.get('blo1')
          score = request.POST.get('score')
          addinfo = Addinfo(name=name,email=email,tech=tech,loc1=loc1,domain=domain,proj=proj,blo1=blo1,score=score)
          addinfo.save()
     return render(request,'addinfo.html')  
def index(request):
     all_developers = Addinfo.objects.all()
     if request.user.is_anonymous:
          return redirect("/login")
     return render(request,"index.html",{'all_developers':all_developers})     
def logoutUser(request):
     logout(request)
     return redirect('/login') 
def search(request):
     q = request.GET.get('q')
     loc = request.GET.get('loc')
     allpost =  Addinfo.objects.filter(loc1=loc,tech=q)
     #allpost = Addinfo.objects.all(title__icontains=query)
     return render(request,"devinfo.html",{'allpost':allpost}) 


     

