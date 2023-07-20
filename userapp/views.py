from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if username == "" or password == "" or repassword == "":
            messages.warning(request, "Please Enter Username and Password")
            return redirect("/register")
        else:
            if password == repassword: 
                if User.objects.filter(username = username).exists():
                    messages.warning(request,"This Username Already Taken")
                    return redirect("/register")
                # สร้างบัญชีผู้ใช้
                else:
                    user = User.objects.create_user(username=username, password=password)
                    user.save()
                    messages.success(request, "Account Created Successfully")
                    return redirect("/register")
                
            else:
                messages.warning(request, "Incorrect Password!")
                return redirect("/register")
    else: 
        return render(request, "register.html")

def login(request):
    if request.method == "POST":
        # รับค่าจากแบบฟอร์ม
        username = request.POST["username"]
        password = request.POST["password"]
        if username == "" or password == "":
            messages.warning(request,"Username or Password is null")
            return redirect("/login")
        else:
            user = auth.authenticate(username=username, password=password)
            if user is not None :
                auth.login(request, user)
                return redirect("/")
            else:
                messages.warning(request,"Username or Password is Invalid")
                return redirect("/login")    
    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect("/login")