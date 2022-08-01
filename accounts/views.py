from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth  import login as auth_login

# Create your views here.
from accounts.forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def signup(request):
    form =SignUpForm()
    if request.method=='POST':
        form =SignUpForm(request.POST)
        if form.is_valid():
            print(form['username'])
            user=form.save()
            auth_login(request,user)
            return redirect('index')
    return render(request,'accounts/signup.html',context={"form":form})