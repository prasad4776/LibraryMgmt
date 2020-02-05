from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter


from .views import BookViewSet, AuthorViewSet, PersonViewSet, IssueViewSet


router = DefaultRouter()
router.register('book', BookViewSet, basename='book')
router.register('author', AuthorViewSet, basename='author')
router.register('person', PersonViewSet, basename='person')
router.register('issue', IssueViewSet, basename='issue')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]
