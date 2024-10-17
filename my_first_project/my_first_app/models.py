"""
This module defines the models for the Django application.
Models:
    Car: Represents a car with a title and year.
    Publisher: Represents a publisher with a name and address.
    Author: Represents an author with a name and birth date.
    Profile: Represents a profile associated with an author, including bio and website.
    Book: Represents a book with a title, publication date, publisher, and multiple authors.
Each model includes a __str__ method to return a string representation of the instance.
"""
from django.db import models


# Create your models here.
class Car(models.Model):
    """
    Car model representing a vehicle with a title and year.

    Attributes:
        title (TextField): The title or name of the car, with a maximum length of 250 characters.
        year (IntegerField): The manufacturing year of the car, which can be null.

    Methods:
        __str__(): Returns a string representation of the car in the format "title - year".
    """
    title = models.TextField(max_length=250)
    year = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.title} - {self.year}"


class Publisher(models.Model):
    """
    Publisher model represents a publishing entity with a name and address.
    Attributes:
        name (TextField): The name of the publisher, with a maximum length of 200 characters.
        address (TextField): The address of the publisher, with a maximum length of 250 characters.
    Methods:
        __str__(): Returns a string representation of the Publisher instance, 
                combining the name and address.
    """
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=250)

    def __str__(self):
        return f"{self.name} - {self.address}"


class Author(models.Model):
    """
    Author model represents an author with a name and birth date.

    Attributes:
        name (TextField): The name of the author, with a maximum length of 200 characters.
        birth_date (DateField): The birth date of the author.

    Methods:
        __str__(): Returns a string representation of the author in the format "name - birth_date".
    """
    name = models.TextField(max_length=200)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.birth_date}"


class Profile(models.Model):
    """
    Profile model representing a user's profile.
    Attributes:
        author (OneToOneField): A one-to-one relationship to the Author model.
        bio (TextField): A text field for the user's biography 
                        with a maximum length of 500 characters.
        website (URLField): A URL field for the user's website.
    Methods:
        __str__(): Returns a string representation of the profile, 
                including the author, bio, and website.
    """
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    website = models.URLField()

    def __str__(self):
        return f"{self.author} - {self.bio} - {self.website}"


class Book(models.Model):
    """
    Book model represents a book entity with its title, publication date, publisher, and authors.

    Attributes:
        title (TextField): The title of the book with a maximum length of 200 characters.
        publication_date (DateField): The date when the book was published.
        publisher (ForeignKey): A foreign key relationship to the Publisher model, 
                                with a cascade delete option.
        authors (ManyToManyField): A many-to-many relationship to the Author model, 
                                    with a related name "authors".

    Methods:
        __str__(): Returns a string representation of the book, including its title, 
                publication date, and publisher.
    """
    title = models.TextField(max_length=200)
    publication_date = models.DateField()
    # author = models.TextField(max_length=200)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name="authors")

    def __str__(self):
        return f"{self.title} - {self.publication_date} - {self.publisher}"
