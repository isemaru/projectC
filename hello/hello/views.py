from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime as dt

def hello_world(request):
    d = {
         'date':dt.now().strftime('%Y/%m/%d')
    }
    return render(request, 'html/hello_world.html', d)


def get_name(request):
    d = {
         'date':dt.now().strftime('%Y/%m/%d')
    }
    return render(request, 'html/get_name.html', d)


def for_name(request):
    seachSetence = request.GET.get('your_name')
    list3 = [[1, 2], [10, 20], [100, 200]]

    d = {
        'your_name': seachSetence,
        'objects': list3,
    }
    return render(request, 'html/for_name.html', d)