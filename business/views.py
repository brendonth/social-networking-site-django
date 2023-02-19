from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.db import models
from .models import profile
from PIL import Image

def business_home(request):
    user = request.user
    biography = models.TextField(default="no bio...", max_length=300)
    context = {
        'buser': user,
        'biography': biography,
    }
    return render(request, 'main/businesshome.html', context)

def business_profile(request):
    user = request.user
    biography = models.TextField(default="no bio...", max_length=300)
    context = {
        'user': user,
        'biography': biography,
    }
    return render(request, 'main/businesshome.html', context)

def business_record(request):
    user = request.user
    biography = models.TextField(default="no bio...", max_length=300)
    context = {
        'user': user,
        'biography': biography,
        # resumes, courseworks, experiences can be in this sheet that they can share when looking for employment
    }
    return render(request, 'main/businesshome.html', context)

def business_store(request):
    user = request.user
    biography = models.TextField(default="no bio...", max_length=300)
    context = {
        'user': user,
        'biography': biography,
        # goods and services posted here for sell. people need proof of identity to do this.
    }
    return render(request, 'main/businesshome.html', context)

def business_zoom(request):
    user = request.user
    biography = models.TextField(default="no bio...", max_length=300)
    context = {
        'user': user,
        'biography': biography,
# they hold meetings and interviews with other companies, employees, acquintances, potential employees etc.
    }
    return render(request, 'main/businesshome.html', context)

def business_jobs(request):
    user = request.user
    biography = models.TextField(default="no bio...", max_length=300)
    context = {
        'user': user,
        'biography': biography,
        #job openings are posted here, companies also can post any openings here
    }
    return render(request, 'main/businesshome.html', context)

def business_resources(request):
    user = request.user
    biography = models.TextField(default="no bio...", max_length=300)
    context = {
        'user': user,
        'biography': biography,
    }
    return render(request, 'main/businesshome.html', context)

