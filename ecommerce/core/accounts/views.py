from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate,login,logout
from .auth import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def user_register(request):
    if request.method == "POST":
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            messages.add_message(request, messages.SUCCESS, 'New user Created')
            return redirect('/register')
        else:
            messages.add_message(request, messages.ERROR, 'user cannot create')
            context = {
                'user' : UserCreationForm
                          }
            return render(request, 'register.html', context)
            
    context = {
        'user' : UserCreationForm
    }

    return render(request, 'register.html', context)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data =form.cleaned_data
            user=authenticate(request, username=data["username"],password=data["password"])
            if user is not None:
                login(request, user)
                return redirect('/dashboard')
            else:
                messages.add_message(request, messages.ERROR, 'user not verified')
                return render( request, 'login.html', {'form': LoginForm})

    context ={
        'form': LoginForm
    }
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    return redirect('/accounts/login')


@login_required
@admin_only
def user_dashboard(request):
    return render(request, 'dashboard.html')

