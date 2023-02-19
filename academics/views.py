from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.db import models
from .models import Profile, ProfileManager, RelationshipManager, Relationship, User
from PIL import Image
from django.db.models import Q
from .forms import ProfileModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def academichome_view(request):
    user = request.user
    #biography = models.TextField(default="no bio...", max_length=300)
    hello = 'Welcome to Brendata World, We have been wait for you!!!'
    context = {
        'user': user,
        'hello': hello,
    }
    return render(request, 'main/academichome.html', context)

@login_required()
def academicprofile_view(request):
    user = request.user
    biography = models.TextField(default="no bio...", max_length=300)
    context = {
        'user': user,
        'biography': biography,
    }

    return render(request, 'academicprofile/my_academicprofile.html', context)

def all_aprofiles(request):
    user = request.user
    biography = models.TextField(default="no bio...", max_length=300)
    context = {
        'user': user,
        'biography': biography,
    }

    return render(request, 'academicprofile/academicprofile_list.html', context)

def academic_request(request):
    user = request.user
    biography = models.TextField(default="no bio...", max_length=300)
    context = {
        'user': user,
        'biography': biography,
    }

    return render(request, 'academicprofile/myacademic_invites.html', context)

def academic_requested(request):
    user = request.user
    biography = models.TextField(default="no bio...", max_length=300)
    context = {
        'user': user,
        'biography': biography,
    }

    return render(request, 'academicprofile/toacademic_invite_list.html', context)


def academic_resources(request):
    uploader = request.user
    #books
    #videos
    #subject

    return render(request, 'main/academichome.html')

def academic_uploads(request):
    #resume
    #other documents
    #free writing
    #plans

    return render(request, 'main/academichome.html')

def academic_record(request):
    #resume
    #other documents
    #free writing
    #plans
    #this will be a sheet that could encompass: work experience, sports, coursework, certificates (uploads), so that they verify and share with others

    return render(request, 'main/academichome.html')

def academic_messages(request):
    #resume
    #other documents
    #free writing
    #plans
    #this can be under dropdown menu

    return render(request, 'main/academichome.html')

def academic_applications(request):
    #resume
    #other documents
    #free writing
    #plans
    #this can be under dropdown menu

    return render(request, 'academics/skillrecord.html')



def dropdown(request):
    #games (academic)
    #other documents
    #settings

    return render(request, 'academics/skillrecord.html')



# profile stuff starts here-------->



