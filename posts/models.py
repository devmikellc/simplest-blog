from datetime import datetime
from re import T
from tkinter.tix import Tree
import django
from django.db import models
from tinymce import models as tinymce_models
from ckeditor.fields import RichTextField
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    # body = tinymce_models.HTMLField() // this works with admin editor
    body = RichTextField(blank=True, null=True)  # this works even with ui and admin
    created_at = models.DateTimeField(
        default=django.utils.timezone.now, blank=True)

    def __str__(self):
        return self.title
