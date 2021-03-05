from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'mijnWebApp/index.html', {})

def contact(request):
    return render(request, 'mijnWebApp/contact.html', {})
