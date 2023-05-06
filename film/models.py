from django.db import models

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField(default=0)
    description = models.TextField()
    poster = models.ImageField(upload_to='filmy/postery')
    url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.title + " (" + str(self.year) + "r.)"