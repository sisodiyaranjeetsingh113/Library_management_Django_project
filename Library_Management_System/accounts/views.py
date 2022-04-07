from django.shortcuts import render, redirect
from accounts.forms import UserAdminCreationForm
from accounts.models import CustomUser

def register(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
    return render(req,'register.html', {'form': form})

def login(req):
    return render(req,'login.html')

from django.contrib.auth import logout

def logout_user(request):
    logout(request)
    return redirect('/')