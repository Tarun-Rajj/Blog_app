from django.db import models

# Create your models here.
class Post(models.Model):  #Here Post is a model which represent the fields title or content and timestamp.
    title = models.CharField(max_length=200)  #In this models.CharField or models.TextField defines the datatype of the fields.
    content = models.TextField()
    author = models.CharField(max_length=14)
    TimeStamp = models.DateTimeField(blank=True)


    def __str__(self):
        return self.title
