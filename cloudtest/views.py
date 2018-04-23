from django.http import HttpResponse
from  django.shortcuts import render
from django.template import loader
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def home(request):
    template = loader.get_template('home.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def room(request):
    template = loader.get_template('rooms-tariff.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def introduction(request):
    template = loader.get_template('introduction.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def gallery(request):
    template = loader.get_template('gallery.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def contact(request):
    template = loader.get_template('contact.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm()

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def signup(request):
    template = loader.get_template('signup.html')
    context = {

    }
    return HttpResponse(template.render(context, request))