from django.http import HttpResponse
from django.template import loader


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