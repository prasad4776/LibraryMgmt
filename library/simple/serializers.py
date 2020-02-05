from rest_framework import serializers
from .models import Person, Issue, Author, Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'b_name', 'price']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'a_name', 'city', 'book']


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id','p_name','username','password','role']


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'book_id', 'person_id', 'issue_date', 'submission_date']
