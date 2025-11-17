from django.db import models

# Create your models here.
class Movie (models.Model):
    title = models.CharField(max_length=30, null=False)
    gender = models.CharField(max_length=30, null=False)
    director_name = models.CharField(max_length=30, null=False)
    year_realase = models.DateField()
    synopsis = models.TextField()
    poster = models.ImageField(upload_to='posters/', null=False, blank=True)

    def __str__(self):
        return self.title