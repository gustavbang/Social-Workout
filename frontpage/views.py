from django.http import HttpResponse


from django.http import Http404
from django.shortcuts import render, redirect
from django.template import loader


from .models import Fitnessguy


def index(request):
    template = loader.get_template('frontpage/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def search(request):
    return redirect('/')


def detail(request, fitnessguy_id):
    try:
        fitGuy = Fitnessguy.objects.get(pk=fitnessguy_id)
    except Fitnessguy.DoesNotExist:
        raise Http404("Fitnessguy does not exist")
    #kan godt køre uden den sidste del (FG)
    return render(request, 'frontpage/detail.html', {'FG': fitGuy})

