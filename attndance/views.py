from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import employeeSerializer
from rest_framework import status
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import employees
import numpy as np
import matplotlib.pyplot as plt
import cv2
#list(employeesl.values("user_id", "name", "addhar"))
@api_view(['GET','POST'])
def userlist(request):
    if request.method == 'GET':
        employeesl=employees.objects.all()
        serialiser=employeeSerializer(employeesl, many=True)
        return Response(serialiser.data)
    if request.method == 'POST':
        serialiser = employeeSerializer(data=request.data)
        if(serialiser.is_valid()):
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        return Response(serialiser.data, status=status.HTTP_400_BAD_REQUEST)
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
