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