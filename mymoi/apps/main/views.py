from django.shortcuts import render , redirect
from django.views import View
from django.conf import settings
from django.forms import modelformset_factory
from .models import MemoirGallery,Memoir
from .forms import MemoirGalleryForm, MemoirForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


#Method 1.   we should everytime send context ={media_url..}
# class MainView(View):
#     def get(self, request ,*args, **kwargs):
#         context={
#             "media_url":settings.MEDIA_URL,

#         }
#         return render(request, "main_app/index.html",context)


#Method2. To solve the issue with the Method 1:
def media_admin(request):
    return{"media_url":settings.MEDIA_URL}

#class base:view class
class MainView(View):
    def get(self, request ,*args, **kwargs):
        memoirs = Memoir.objects.all()
        return render(request, "main_app/index.html",{"memoirs":memoirs})
#=======================================================================================
#5.2
#view for  images and text of  Memoir:view Function:A function which can get a Memoir
@login_required
def add_memoir(request):  # sourcery skip: remove-pass-elif, remove-unnecessary-else, swap-if-else-branches, switch
    ImageFormSet = modelformset_factory(MemoirGallery, form =MemoirGalleryForm, extra=4)
    if request.method =='GET':
        memoir_form = MemoirForm()
        image_formset=ImageFormSet(queryset=MemoirGallery.objects.none(),)
        context={
            "memoir_form":memoir_form,
            "image_formset":image_formset
        }
        return render(request, 'main_app/register_memoir.html' ,context)
    elif request.method =='POST':
        memoir_form=MemoirForm(request.POST)
        image_formsset = ImageFormSet(request.POST,request.FILES)
        if memoir_form.is_valid() and image_formsset.is_valid():
            memo_obj = memoir_form.save() #memoir is saved
            for form in image_formsset.cleaned_data:
                if form:
                    MemoirGallery.objects.create(
                        Memoir_image_name = form['Memoir_image_name'],
                        memoir= memo_obj
                    )
            messages.success(request, 'SAVED your Memoir  Successfully Done','success')
            return redirect('main:index')
        else:
            return render(request, 'main_app/register_memoir.html',{ "memoir_form":memoir_form })



