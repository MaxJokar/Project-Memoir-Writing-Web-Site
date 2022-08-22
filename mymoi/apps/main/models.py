from django.db import models
from django.utils import timezone
from apps.account.models import CustomUser

# install crispy library helps to have text and images from 2 tables in one together
#pip install django-crispy-form: setting add INSTALLED_APPS:crispy_forms


class Memoir(models.Model):
    memoir_title = models.CharField(max_length=200, verbose_name='Memoir Title ')
    Memoir_text = models.TextField(verbose_name='Memoir Text ')
    register_data = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)
    user_registered = models.ForeignKey(CustomUser, on_delete = models.CASCADE,null=True)

    def __str__(self):
        return self.memoir_title





# for related_name , we should define a funcation to control in which the pic must be uploaded!
def upload_gallery_image(instance , filename):
    return f"images/memoir/{instance.memoir.memoir_title}/gallery/{filename}"

class MemoirGallery(models.Model):
    Memoir_image_name = models.ImageField(upload_to=upload_gallery_image,verbose_name='Memoir Image ')
    memoir=models.ForeignKey(Memoir, on_delete=models.CASCADE,null=True, related_name='images')






class MemoirLike(models.Model):
    user_liked = models.ForeignKey(CustomUser,  on_delete = models.CASCADE,null=True)
    memoir = models.ForeignKey(Memoir, on_delete=models.CASCADE,null=True)


















