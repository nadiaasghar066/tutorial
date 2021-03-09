from django.shortcuts import render
from django.contrib.auth.models import User
from snippets.models import book
from snippets.models import auther
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from snippets.serializers import BookSerializer
from snippets.serializers import AutherSerializer
from rest_framework import generics
from snippets.serializers import UserSerializer
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('book-list', request=request, format=format),
        'auther': reverse('auther-list', request=request, format=format),
    })
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        book = self.get_object()
        return Response(book.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class autherViewSet(viewsets.ModelViewSet):
    queryset = auther.objects.all()
    serializer_class = AutherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        auther = self.get_object()
        return Response(auther.highlighted)