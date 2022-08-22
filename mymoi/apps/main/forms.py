from django import forms
from .models import Memoir , MemoirGallery

#Form for Momoir
class MemoirForm(forms.ModelForm):
    class Meta:
        model = Memoir
        fields = ['memoir_title','Memoir_text']




#Form for Gallery
class MemoirGalleryForm(forms.ModelForm):
    class Meta:
        model = MemoirGallery
        fields = ['Memoir_image_name']

