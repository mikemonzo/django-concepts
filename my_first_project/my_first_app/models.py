from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.TextField(max_length=250)
    year = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.title} - {self.year}"


class Publisher(models.Model):
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=250)
    

    def __str__(self):
        return f"{self.name} - {self.address}"




class Author(models.Model):
    name = models.TextField(max_length=200)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.birth_date}"


class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    website = models.URLField()
    

    def __str__(self):
        return f"{self.author} - {self.bio} - {self.website}"


class Book(models.Model):
    title = models.TextField(max_length=200)
    publication_date = models.DateField()
    # author = models.TextField(max_length=200)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name="authors")

    def __str__(self):
        return f"{self.title} - {self.publication_date} - {self.publisher}"
    
