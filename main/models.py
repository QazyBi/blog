from django.db import models
from tinymce.models import HTMLField


class Blog(models.Model):
    publication_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    title = models.CharField(max_length=100)
    text = HTMLField()
    image = models.ImageField(upload_to='article_pics')

    def __str__(self):
        return self.text[:80]
