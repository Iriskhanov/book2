from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.FileField(upload_to='static/images')
    def __repr__(self):
        return self.name
