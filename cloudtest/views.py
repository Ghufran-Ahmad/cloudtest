from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login


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


def profile(request):
    if request.method == 'POST':
        user = request.user
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        image = request.FILES.get('image')
        if image is not None:
            user.profile.display_picture = image
        if password is not None and password !="":
            user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        return redirect('profile')
    if request.method == 'GET':
        return render('profile.html')


def contact(request):
    template = loader.get_template('contact.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def loginp(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is None:
            return render(request, 'login.html')
        else:
            login(request, user)
            return render(request, 'home.html')
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == "GET":
        template = loader.get_template('signup.html')
        context = {

        }

        return HttpResponse(template.render(context, request))
    if request.method == "POST":
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        username = name

        firstname = name.strip().split(' ')[0]
        lastname = ' '.join((name + ' ').split(' ')[1:]).strip()

        if username and password:
            user, created = User.objects.get_or_create(username=username, email=email, first_name=firstname,
                                                       last_name=lastname)

            if created:
                user.set_password(password)
                user.save()

            user = authenticate(username=username, password=password)
            login(request, user)

            return render(request, 'home.html')
    else:
        return render(request, 'signup.html')