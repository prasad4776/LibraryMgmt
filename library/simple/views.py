from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication

from .models import Book, Author, Issue, Person
from .serializers import BookSerializer, AuthorSerializer, IssueSerializer, PersonSerializer
from rest_framework.permissions import IsAuthenticated


class BookViewSet(ViewSet):
    serializer_class = BookSerializer

    # permission_classes = (IsAuthenticated)

    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request):
        data = request.data
        print(data)
        queryset = Book.objects.create(b_name=data['b_name'], price=data['price'])
        serializer = BookSerializer(queryset)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Book.objects.get(id=pk)
        print(queryset)
        serializer = BookSerializer(queryset)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Book.objects.get(id=pk).delete()
        return Response({'message': 'successfully deleted', 'status': 200, 'queryset': queryset})

    # def partial_update(self, request, pk=None):
    #     book = get_object_or_404(Book, pk=pk)
    #     book.b_name = request.data['b_name']
    #     book.save()
    #     serializer = BookSerializer(book)
    #     return Response(serializer.data)

    def update(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)
        book.b_name = request.data['b_name']
        book.price = request.data['price']
        book.save()
        serializer = BookSerializer(book)
        return Response(serializer.data)


class AuthorViewSet(ViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def list(self, request):
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        author = Author.objects.create(a_name=data['a_name'], city=data['city'])
        author.book.add(data['book'])
        author.save()
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Author.objects.get(id=pk)
        print(queryset)
        serializer = AuthorSerializer(queryset)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Author.objects.get(id=pk).delete()
        return Response({'message': 'successfully deleted', 'status': 200, 'queryset': queryset})

    def update(self, request, pk=None):
        author = get_object_or_404(Author, pk=pk)
        author.a_name = request.data['a_name']
        author.city = request.data['city']
        author.book.add(request.data['book'])
        author.save()
        serializer = AuthorSerializer(author)
        return Response(serializer.data)


class PersonViewSet(ViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def list(self, request):
        queryset = Person.objects.all()
        serializer = PersonSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Person.objects.get(id=pk)
        print(queryset)
        serializer = PersonSerializer(queryset)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Person.objects.get(id=pk).delete()
        return Response({'message': 'successfully deleted', 'status': 200, 'queryset': queryset})

    def create(self, request):
        data = request.data
        print(data)
        queryset = Person.objects.create(p_name=data['p_name'], username=data['username'],
                                              password=data['password'],
                                              role=data['role'])
        serializer = PersonSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, pk=None):
        person = get_object_or_404(Person, pk=pk)
        person.p_name = request.data['p_name']
        person.username = request.data['username']
        person.password = request.data['password']
        person.role = request.data['role']
        serializer = PersonSerializer(person)
        return Response(serializer.data)


class IssueViewSet(ViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def list(self, request):
        queryset = Issue.objects.all()
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Issue.objects.get(id=pk)
        print(queryset)
        serializer = IssueSerializer(queryset)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Issue.objects.get(id=pk).delete()
        return Response({'message': 'successfully deleted', 'status': 200, 'queryset': queryset})

    def create(self, request):
        book = Book.objects.get(id=request.data['book_id'])
        person = Person.objects.get(id=request.data['person_id'])
        issue = Issue.objects.create(book_id=book, person_id=person,
                                     issue_date=request.data['issue_date'],
                                     submission_date=request.data['submission_date'])
        issue.save()
        serializer = IssueSerializer(issue)
        return Response(serializer.data)

    def update(self, request, pk=None):
        issue = get_object_or_404(Issue, pk=pk)
        issue.issue_date = request.data['issue_date']
        issue.submission_date = request.data['submission_date']
        issue.book_id = Book.objects.get(id=request.data['book_id'])
        issue.person_id = Person.objects.get(id=request.data['person_id'])

        issue.save()
        serializer = IssueSerializer(issue)
        return Response(serializer.data)

# class LoginViewSet(ViewSet):
#     def create(self, request):
#         user = Person.objects.get(username=request.data['username'])
#         if user:
#             if user.password == request.data['password']:
#                 return Response({'message': 'login successful', 'token': ObtainAuthToken().post(request)})
#             else:
#                 return Response({'message': 'Invalid password'})
#         return Response({'message': 'Invalid username'})
