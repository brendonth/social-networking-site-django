from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from PIL import Image
from django.db import models



def home_view(request):
    user = request.user
    hello = 'Welcome to Brendata World, We have been wait for you!!!'
    context = {
        'user': user,
        'hello': hello,
    }
    return render(request, 'main/home.html', context)
    # return HttpResponse('Welcome to Brendata World, We have been wait for you!!!')

def groups_view(request):
    user = request.user
    hello = 'are you a group?'
    context = {
        'user': user,
        'hello': hello,


    }
    return render(request, 'main/groups.html', context)
    # return HttpResponse('are you a group?')


def messages_view(request):
    user = request.user
    hello = 'you have messages here!'
    context = {
        'user': user,
        'hello': hello,
    }
    return render(request, 'message/messagehome.html', context)
   # return HttpResponse('you have messages here!')

def tutor_view(request):
    user = request.user
    biography = models.TextField(default="no bio...", max_length=300)
    context = {
        'user': user,
        'biography': biography,
    }
    return render(request, 'main/academics.html', context)