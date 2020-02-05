from django.contrib import admin
from .models import Book,Author,Issue,Person
# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Issue)
admin.site.register(Person)