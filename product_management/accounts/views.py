from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email =request.POST['email']
        password1= request.POST['password1']
        password2= request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('username exits.... try with anothernamee')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    print('Eamail is already taken... try anotherone')
                    return redirect('register')
                else:
                    user =User.objects.create_user(username=username,email=email,password=password1)
                    user.save()
                    return redirect('login')
        else:
            print('password did not match')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')

@never_cache
def login(request):
    if request.method == "POST": #if the cndtn is true it shoulbe enter into the if condition
        username= request.POST['username']
        password=request.POST['password1']
        user = auth.authenticate(username=username,password=password)
        if User is not None:
            auth.login(request,user)
            print('login is sucessfully')
            return redirect('showproducts')
        else:
            print('invalid credentials')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')
@login_required(login_url="login")  
@never_cache
def logout(request):
     if request.method == 'POST':
        auth.logout(request)
        print('logout sucessfully from website')
        return redirect('login')
    

