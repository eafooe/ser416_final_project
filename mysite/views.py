from django.http import HttpResponse, HttpResponseNotAllowed
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from users.forms import CustomUserCreationForm
def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'registration/login.html')

# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            role = form.cleaned_data.get('role')
            first_name = form.cleaned_data.get('first_name')
            user = authenticate(email=email, password=raw_password)
            login(request)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def logout(request):
    logout(request)

def about(request):
    return render(request, 'about.html')

def calendar(request):
    return render(request, 'calendar.html')

def programs(request):
    return render(request, 'programs.html')

def contact(request):
    return render(request, 'contact.html')

def facilities(request):
    return render(request, 'facilities.html')

def donate(request):
    return render(request, 'donate.html')

def reservations(request):
    return render(request, 'reservations.html')

def profile(request):
    return render(request, 'profile.html')
