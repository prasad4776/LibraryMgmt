from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser


# Create your models here.

class Book(models.Model):
    b_name = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.b_name} ki price h {self.price}'


class Author(models.Model):
    a_name = models.CharField(max_length=20)
    city = models.CharField(max_length=10)
    book = models.ManyToManyField(Book)

    def __str__(self):
        return self.a_name


class Person(models.Model):
    p_name = models.CharField(max_length=20, null=True, blank=True)
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=10)

    def __str__(self):
        return self.p_name


class Issue(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    issue_date = models.DateField()
    submission_date = models.DateField()

    def __str__(self):
        return str(self.issue_date)
