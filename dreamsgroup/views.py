from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from account.models import Users
from dreamsgroup.models import Events, College, Post, School
from DreamsTrack.views import getid
import datetime
from dreamsgroup.forms import postform
from django.core.urlresolvers import reverse


def dreamsmain(request):
    name = getid(request)
    return render(request, 'dgroup/dreamsmain.html', {'name': name})


def events(request):
    try:
        state = request.GET['state']
        event = Events.objects.filter(state__iexact=state)
        return render(request, 'dgroup/events-result.html', {'event': event})
    except:
        return render(request, 'dgroup/events-result.html', {'event': ""})


def myCollege(request):
    name = getid(request)
    if name == "":
        return render(request, 'dgroup/mycollege.html', {'name': name})
    col = name.college
    users = Users.objects.filter(college__iexact=col)
    college = College.objects.get(name__iexact=col)
    event = Events.objects.filter(college__iexact=col)
    post = Post.objects.filter(user=name.id, collegeName__iexact=col).order_by('-date')
    return render(request, 'dgroup/mycollege.html',
                  {'name': name, 'college': college, 'posts': post, 'user': users, 'events': event, 'col':1})


def mySchool(request):
    name = getid(request)
    if name == "":
        return render(request, 'dgroup/mycollege.html', {'name': name})
    col = name.school
    users = Users.objects.filter(school__iexact=col)
    school = School.objects.get(name__iexact=col)
    event = Events.objects.filter(college__iexact=col)
    post = Post.objects.filter(user=name.id, collegeName__iexact=col).order_by('-date')
    return render(request, 'dgroup/mycollege.html',
                  {'name': name, 'college': school, 'posts': post, 'user': users, 'events': event,'col':2})


def writepost(request):
    name = getid(request)
    cars = request.GET['cars']
    if cars == "1":
        col = name.college
        college = College.objects.get(name__iexact=col)
    else:
        col = name.school
        college = School.objects.get(name__iexact=col)
    content = request.GET['content']
    if content == "" or content == " " or content == "Write Here!":
        return render(request, 'dgroup/writepost.html', {'content': "Empty"})
    post = Post(content=content, date=datetime.datetime.now(), user=name.id, userName=name, college=college.id, collegeName=college)
    post.save()
    return render(request, 'dgroup/writepost.html')

def uploadpicture(request):
    name = getid(request)
    cars = request.POST['cars']
    if cars == "1":
        col = name.college
        college = College.objects.get(name__iexact=col)
        next = "/dreamsgroup/mycollege/"
    else:
        col = name.school
        college = School.objects.get(name__iexact=col)
        next = "/dreamsgroup/myschool/"
    file = request.FILES['image']
    content = request.POST['content']
    post = Post(image=file, date=datetime.datetime.now(), user=name.id, userName=name, college=college.id, collegeName=college,content=content)
    post.save()
    return render(request, 'dgroup/writepost.html',{'next':next})

def uploadvideos(request):
    name = getid(request)
    cars = request.POST['cars']
    if cars == "1":
        col = name.college
        college = College.objects.get(name__iexact=col)
        next = "/dreamsgroup/mycollege/"
    else:
        col = name.school
        college = School.objects.get(name__iexact=col)
        next = "/dreamsgroup/myschool/"
    video = request.POST['video']
    content = request.POST['content']
    post = Post(video=video, date=datetime.datetime.now(), user=name.id, userName=name, college=college.id, collegeName=college,content=content)
    post.save();
    return render(request, 'dgroup/writepost.html',{'next':next})