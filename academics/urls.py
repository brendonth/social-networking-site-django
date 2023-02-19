from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from .views import academichome_view, academicprofile_view, academic_resources, academic_record,academic_messages, academic_uploads, all_aprofiles,academic_request, academic_requested


app_name = 'academics'

urlpatterns = [
    path('', academichome_view, name='academichome-view'),
    path('resources/', academic_resources, name= 'academic-resources'),
    path('profile/', academicprofile_view, name= 'academicprofile-view'),
    path('record/', academic_record, name='academic-record'),
    path('messages/', academic_messages, name='academic-messages'),
    path('uploads/', academic_uploads, name='academic-uploads'),
    path('academicprofile', include('academicprofile.urls', namespace='academicprofiles')),
    path('allacademicprofile', all_aprofiles, name ='allacademicprofiles'),
    path('academicrequests', academic_request, name = 'academicrequest'),
    path('academicrequested', academic_requested, name = 'academicrequested'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
