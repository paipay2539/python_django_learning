from django.db import models

# Create your models here.

# https://www.youtube.com/watch?v=1W2ABfy487s
class Post(models.Model):
    title = models.CharField(max_length=100) # normal text
    body = models.TextField() # box text

# id (1 auto) , title (2), body (3)

# python manage.py makemigrations 
# to gen models (table django) to migration (0001_initial) 
# python manage.py migrate 
# to push migration (0001_initial) to database

    def __str__(self) : # to convert return value to title name each Post
        return self.title