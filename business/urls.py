from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import business_home, business_zoom, business_store, business_profile, business_record, business_resources, business_jobs

app_name = 'business'

urlpatterns = [
    path('', business_home, name='business-home'),
    path('resources/', business_resources, name='business-resources'),
    path('zoom/', business_zoom, name='business-zoom'),
    path('store/', business_store, name='business-store'),
    path('profile/', business_profile, name='business-profile'),
    path('record/', business_record, name='business-record'),
    path('jobs/', business_jobs, name='business-jobs')

]