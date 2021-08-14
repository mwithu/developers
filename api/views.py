from django.shortcuts import render
from django.http import HttpResponse
from .models import UserDetail, Credential
from .serializers import UserDetailsSerializer, CredentialSerializer
from rest_framework import viewsets

class UserDetailsViewSet(viewsets.ModelViewSet):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailsSerializer

class CredentialViewSet(viewsets.ModelViewSet):
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer

def userDetails(request, pageName):
    if(pageName != 'userdetails'):
        return HttpResponse("<h1>Page does not exist</h1>")
