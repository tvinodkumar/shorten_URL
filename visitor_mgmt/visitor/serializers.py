from rest_framework import serializers
from rest_framework.authtoken.models import Token
from . models import Shorten_URLS


class ShortenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shorten_URLS
        fields = ['shorten_url', 'url_name']
