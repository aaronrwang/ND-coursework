# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .signup_form import CreateNewUserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def sign_up_view(request):
    if request.method == 'POST':

        # Creates a new user on post request
        form = CreateNewUserProfile(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['firstname']
            user.last_name = form.cleaned_data['lastname']
            user.email = form.cleaned_data['email']
            user.save()
            login(request, user)

            # Go to listings on success
            return redirect('browse_listings')
    # Load the form on a get request
    else:
        form = CreateNewUserProfile()
    
    # if already logged in redirect
    if request.user.is_authenticated:
        return redirect('browse_listings')

    return render(request, 'accounts/sign_up.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # See if the username and password are valid
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('browse_listings')
        # Handle wrong username/password
        else:
            messages.error(request, "Incorrect username or password here.")
    
    # if already logged in redirect
    if request.user.is_authenticated:
        return redirect('browse_listings')
    
    # return log in form
    return render(request, 'accounts/login.html')

# Logs the user out
def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('home')

        