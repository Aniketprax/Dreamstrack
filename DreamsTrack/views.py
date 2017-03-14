from django.shortcuts import render
from account.views import Users

def index(request):
    name=getid(request)
    return render(request, 'Index.html',{'name':name})

def getid(request):
    name=""
    try:
        ids=request.session['id']
        name = Users.objects.get(id=ids)
    except:
        pass
    return name