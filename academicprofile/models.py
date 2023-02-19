from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

import profiles.models
from .utils import get_random_code
from django.template.defaultfilters import slugify
from django.db.models import Q

# Create your models here.

class aProfileManager(models.Manager):

    def get_all_aprofiles_to_invite(self, sender):
        profiles = aProfile.objects.all().exclude(user=sender)
        profile = aProfile.objects.get(user=sender)
        qs = Relationship.objects.filter(Q(sender=profile) or Q(receiver=profile))
        print(qs)
        print("########")

        accepted = set([])
        for rel in qs:
            if rel.status == 'accepted':
                accepted.add(rel.receiver)
                accepted.add(rel.sender)
        print(accepted)
        print("########")

        available = [profile for profile in profiles if profile not in accepted]
        print(available)
        print("########")
        return available


    def get_all_aprofiles(self, me):
        profiles = aProfile.objects.all().exclude(user=me)
        return profiles


class aProfile(models.Model):
    business_name = models.CharField(max_length=200, blank=True)
    business_type = models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.CharField(default="business type...", max_length=200)
    bio = models.TextField(default="no bio...", max_length=300)
    email = models.EmailField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(default='avatar.png', upload_to='avatars/')
    afriends = profiles.models.Profile
    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = aProfileManager()

    def __str__(self):
        return f"{self.user.username}-{self.created.strftime('%d-%m-%Y')}"

    def get_absolute_url(self):
        return reverse("academicprofile:profile-detail-view", kwargs={"slug": self.slug})

    def get_friends(self):
        return self.afriends.all()

    def get_friends_no(self):
        return self.afriends.all().count()

    def get_posts_no(self):
        return self.posts.all().count()

    def get_all_authors_posts(self):
        return self.posts.all()

    def get_likes_given_no(self):
        likes = self.like_set.all()
        total_liked = 0
        for item in likes:
            if item.value=='Like':
                total_liked += 1
        return total_liked

    def get_likes_received_no(self):
        posts = self.posts.all()
        total_liked = 0
        for item in posts:
            total_liked += item.liked.all().count()
        return total_liked


    __initial_business_name = None
    __initial_business_type = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initial_business_name = self.business_name
        self.__initial_business_type = self.business_type

    def save(self, *args, **kwargs):
        ex = False
        to_slug = self.slug
        if self.business_name != self.__initial_business_name or self.business_type != self.__initial_business_type or self.slug=="":
            if self.business_name and self.business_type:
                to_slug = slugify(str(self.business_name) + " " + str(self.business_type))
                ex = aProfile.objects.filter(slug=to_slug).exists()
                while ex:
                    to_slug = slugify(to_slug + " " + str(get_random_code()))
                    ex = aProfile.objects.filter(slug=to_slug).exists()
                else:
                    to_slug = str(self.user)
                self.slug = to_slug
                super().save(*args, **kwargs)

STATUS_CHOICES = (
    ('send', 'send'),
    ('accepted', 'accepted')
)

class RelationshipManager(models.Manager):
    def invitations_received(self, receiver):
        qs = Relationship.objects.filter(receiver=receiver, status='send')
        return qs


class Relationship(models.Model):
    sender = models.ForeignKey(aProfile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(aProfile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = RelationshipManager()

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"



