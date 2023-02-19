from django import forms
from .models import aProfile

class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = aProfile
        fields = ('business_name', 'business_type', 'category', 'bio', 'avatar')