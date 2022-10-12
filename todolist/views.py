from http.client import HTTPResponse
from todolist.models import Task

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core import serializers


import datetime
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse

from .forms import TaskForm


# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    user = request.user
    data_todolist = Task.objects.filter(user=user)
    context = {
        'list_todolist': data_todolist,
    }
    return render(request, 'todolist.html', context)

@login_required(login_url='/todolist/login/')
def show_todolist_json(request):
    user = request.user
    data_todolist = serializers.serialize("json", Task.objects.filter(user=user))
    return HttpResponse(data_todolist, content_type="application/json")

def task_delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return show_todolist(request)

def task_toggle(request, id):
    task = Task.objects.get(id=id)
    if task.is_finished:
        task.is_finished = False
    else:
        task.is_finished = True
    task.save()
    return show_todolist(request)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Invalid Username or Password!')
    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

@login_required(login_url='/todolist/login/')
def create_task(request): ####    
    form = TaskForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            return response
    context = {'form': form}
    return render(request, 'create_task.html', context)

    # if request.method == 'POST':
    #     user = request.user
    #     title = request.POST.get("title")
    #     description = request.POST.get("description")

    #     new_task = Task(user=user, title=title, description=description)
    #     new_task.save()

    #     return HttpResponse(b"CREATED", status=201)
    # return HttpResponseNotFound()

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response