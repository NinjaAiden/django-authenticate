from django.shortcuts import render, HttpResponse, redirect, reverse
from djang.contrib import auth

def index(request):
    """ Return index html file """
    return render(request, "index.html")

def logout(request):
    """ Log the user out """
    auth.logout(request)
    return redirect(reverse('index'))