from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from snippets.views import BookViewSet, UserViewSet, api_root, autherViewSet
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

book_list = BookViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
book_detail = BookViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
book_highlight = BookViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
auther_list = autherViewSet.as_view({
    'get': 'book-list'
})
auther_detail = autherViewSet.as_view({
    'get': 'book-list'
})
urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('snippets/', book_list, name='book-list'),
    path('snippets/<int:pk>/', book_detail, name='book-detail'),
    path('snippets/<int:pk>/highlight/', book_highlight, name='book-highlight'),
    path('users/', user_list, name='user-list'),
    path('', views.api_root),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    path('auther/', auther_list, name='auther-list'),
])
router = DefaultRouter()
router.register(r'snippets', views.BookViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'auther', views.autherViewSet)
urlpatterns = [
    path('', include(router.urls)),
]