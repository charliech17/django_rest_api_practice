from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *


# Create your views here.
@api_view(['GET', 'POST'])
def get_all_student(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_student_detail(request,id):
    if request.method == 'GET':
        student = get_object_or_404(Student,pk=id)
        serializers = StudentSerializer(student)
        return Response(serializers.data)
    

@api_view(['GET'])
def student_by_age(request,gt_age):
    if request.method == 'GET':
        student = Student.objects.filter(age__gt=gt_age) #name__exact
        serializers = StudentSerializer(student,many=True)
        return Response(serializers.data)
    
@api_view(['GET','Post'])
def get_all_course(request):
    if request.method == 'GET':
        courses = CoursesInfo.objects.all()
        serializer = CoursesInfoSerializer(courses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CoursesInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','Post'])
def add_std_course(request):
    if request.method == 'GET':
        return Response("ok")
    elif request.method == 'POST':
        serializer = PostStdStatusSerializer(
            data=request.data,
            context={
                "std_name": request.data["std_name"],
                "std_course": request.data["std_course"]
            }
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
