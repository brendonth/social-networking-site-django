from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from profiles.models import Profile

from django.template.defaultfilters import slugify
from django.db.models import Q
# Create your models here.

class profile(models.Model):
    student_name = models.CharField(max_length=200, blank=True)
    #school_level = models.Choices('pre-k', 'primary', 'high school', 'undergrad', 'grad', 'postgrad', 'independent')
#    subjects = models.Choices('biology', 'maths', 'english')
    #academic_record = models.FileField (upload_to='/static')
#    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio...", max_length=300)