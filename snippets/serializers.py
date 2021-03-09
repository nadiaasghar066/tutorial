from rest_framework import serializers
from django.contrib.auth.models import User
from snippets.models import book, LANGUAGE_CHOICES, STYLE_CHOICES, auther
from snippets.permissions import IsOwnerOrReadOnly

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = book
        fields = ['url', 'bookname']


class AutherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = auther
        fields = ['id', 'url', 'name', 'bookname']



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username']