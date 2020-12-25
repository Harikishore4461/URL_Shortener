from django.db import models

# Create your models here.
class Url(models.Model):
    original_url = models.URLField(max_length=500)
    shorten_url = models.CharField(max_length=200)
    visited = models.IntegerField(default=0)
    Time_url_created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.original_url
