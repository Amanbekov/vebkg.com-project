from django.shortcuts import render


from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions
from apps.company.models import Company
from apps.video.models import Video
from apps.video.serializers import VideoSerializer

class VideoView(ModelViewSet):
    queryset= Video.objects.all()
    serializer_class=VideoSerializer
