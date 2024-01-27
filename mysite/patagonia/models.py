from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class portfolo(models.Model):
    slug= models.SlugField(blank=True)
    h1_tag= models.CharField(max_length=150)
    title= models.CharField(max_length=150)
    description=models.CharField(max_length=200)
    duree= models.CharField(max_length=40)
    designtool= models.ImageField(upload_to="static/images")
    devtool= models.ImageField(upload_to="static/images")
    siteimages= models.ImageField(upload_to="static/images")
    showone= models.ImageField(upload_to="static/images", blank=True)
    text_info=RichTextUploadingField(max_length=3000)
    website= models.URLField(max_length=100, blank=True)
    loom_video = models.URLField(blank=True)