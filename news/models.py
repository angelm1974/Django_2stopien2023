from django.db import models

# Create your models here.
class News(models.Model):
    naglowek=models.CharField(max_length=200)
    tresc=models.TextField()
    data=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.naglowek
    
    class Meta:
        verbose_name_plural='Newsy'
        verbose_name='News'
        ordering=['-data']    