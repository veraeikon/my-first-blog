from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.urls import reverse

from django.forms import ModelForm


class Post(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default = timezone.now)
    published_date = models.DateTimeField(
            blank = True, null = True)
    slug = models.SlugField(max_length = 40, unique = True)
    
    def get_absolute_url(self):
        return reverse ('post_detail', args = (self.slug,))
    
    def publish (self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title
    
    def slug(self):
        slugify(self.title)

class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE )
    photo = models.FileField(upload_to="images/")    
    upload_date=models.DateTimeField(auto_now_add =True)

# FileUpload form class.
class UploadForm(ModelForm):
    class Meta:
        model = Photo
        fields = ('photo',)