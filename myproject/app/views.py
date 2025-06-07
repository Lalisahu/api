from django.shortcuts import render,HttpResponse
from datetime import *


def app(request):
    return HttpResponse("Hello, world. You're at the app index.")
def set(request):
    data = render(request, 'app/set.html')
    data.set_cookie('name', 'lalit')
    data.set_cookie('age', '22')
    data.set_cookie('date', 'bhopal')
    return data
def get(request):
    print('get_cookies')
    request.COOKIES
    name = request.COOKIES.get('name')
    age = request.COOKIES.get('age')
    date = request.COOKIES.get('date')
    
    data={
        'name': name,
        'age': age,
        'date': date
    }
    return render(request, 'get.html', {'data': data})

# Create your views here.
