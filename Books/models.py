from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    embg = models.CharField(max_length=13)
    year_of_birth = models.IntegerField()
    country = models.CharField(max_length=50)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.first_name+" "+self.last_name


class Publication(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    address1 = models.CharField(max_length=50)
    house_number = models.CharField(max_length=10)
    city = models.CharField(max_length=15)
    country = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    publication = models.ForeignKey(Publication, on_delete=models.SET_NULL, null=True)
    isbn = models.CharField(max_length=17)
    content = models.TextField(null=True, blank=True)


class PublicationAuthor(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    publication = models.ForeignKey(Publication, on_delete=models.SET_NULL, null=True)
