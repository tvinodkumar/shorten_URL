from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Shorten_URLS
from rest_framework import generics
from . import serializers
from rest_framework import status
from . serializers import ShortenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from django.template import RequestContext
# Create your views here.

# ##########################################################


def index(request):
    return render(request, 'index.html')


def create_shorten_url(request):
    return render(request, 'shorten_url_create.html')


def list_shorten_url(request):
    shorten_url_list = Shorten_URLS.objects.all()
    return render(request, 'shorten_url_list.html', {'shorten_url_list': shorten_url_list})


def shorten_URL_View(request):
    shorten_url = request.POST.get('shorten_url')
    url_name = request.POST.get('url_name')
    sh_url = Shorten_URLS(shorten_url=shorten_url, url_name=url_name)
    sh_url.save()
    return HttpResponse("Shorten_url Inserted Successfully")


# API's , getting triggered from POSTMAN
class Shorten_URLs_API_Class(APIView):

    def post(self, request, format=None):
        serializer = serializers.ShortenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Shorten URL is inserted successfully", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        visitors = Shorten_URLS.objects.all()
        serializer = serializers.ShortenSerializer(visitors, many=True)
        return Response(serializer.data)
