from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Employees
from . serializers import EmployeesSerializer


class EmployeeList(APIView):

    def get(self, request):
        employees1 = Employees.objects.all()
        serializer = EmployeesSerializer(employees1, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = EmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employees1 = Employees.objects.get(pk=pk)
        employees1.delete()
        return Response(status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        employees1 = Employees.objects.get(pk=pk)
        serializer = EmployeesSerializer(employees1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





