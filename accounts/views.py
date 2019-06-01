from django.shortcuts import render, HttpResponse

def index(request):
    """ Return index html file """
    return render(request, "index.html")