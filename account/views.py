from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers import json
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from account.forms import RegisterForm,LoginForm
from account.models import Users


def getid(request):
    name=""
    try:
        ids=request.session['id']
        name = Users.objects.get(id=ids)
    except:
        pass
    return name

def connect(request):
    Rform=RegisterForm
    return render(request, 'connect.html')

def register(request):
    name = "OLA"
    if request.method == "POST":
        mlf = RegisterForm(request.POST)
        if mlf.is_valid():
            mlf.save()
            email=mlf.cleaned_data['email']
            password = mlf.cleaned_data['password']
            try:
                name = Users.objects.get(email=email, password=password)
            except ObjectDoesNotExist:
                pass
        else:
            name="NOT VALID"
    else:
        name = "Error"
    form = RegisterForm(request.POST)
    return render(request, 'register.html', {"name": name, "phno": form})


def login(request):
    nexturl=request.GET['next']
    if request.method == 'POST':
        logform = LoginForm(request.POST)
        if logform.is_valid():
            email = logform.cleaned_data['email']
            password = logform.cleaned_data['password']
            try:
                name = Users.objects.get(email=email, password=password)
                request.session['id'] = name.id
                return render(request, 'login.html', {'name': name, 'nexturl':nexturl})
            except:
                return HttpResponse("<h1>Invalid User Name or Password</h1>")
        else:
            return HttpResponse("<h1>You left a field empty</h1>")


def logout(request):
    try:
        del request.session['id']
        del request.session['cart']
    except KeyError:
      pass
    return render(request, 'loggedout.html')


def dreamsjob(request):
    name = getid(request)
    array = ([
        ['Year', 'Sales', 'Expenses'],
        ['2004', 1000, 400],
        ['2005', 1170, 460],
        ['2006', 660, 1120],
        ['2007', 1030, 540]
    ])
    return render_to_response('dreamsjob.html',{'name':'array'})

