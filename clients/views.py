from django.http import HttpResponse
from django.shortcuts import render


def do_calculations(value1, value2):
    return value1 * value2


def test_function(request):
    todo = do_calculations(30, 4)
    p_flag = True
    people = ['Raymond', 'Chacha', 'Abuba', 'Davie', 'Timoth', 'deo']
    return render(request, 'index.html', {'total': todo, 'people': people, 'p_flag': p_flag})


def list_clients(request):
    return HttpResponse('Hello world')


def special_case_2003(request):
    return HttpResponse('Home sweet home')


def special_case(request, year):
    return HttpResponse('Home sweet year will be %s' % year)


def month_archive(request, year, month):
    return HttpResponse('Home of %s and %s' % (year, month))
