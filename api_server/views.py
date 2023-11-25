from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *
from .permissions import CustomPermission


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
        # 依照姓名及年齡去排序
        stdCourseStatus = StdCourseStatus.objects \
                            .select_related("students","courses") \
                            .order_by("students__name","students__age") \
                            .all()
        serializer = StdCourseStatusSerializer(stdCourseStatus,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        std_name = request.data.pop("std_name")
        std_course = request.data.pop("std_course")
        courses_id = CoursesInfo.objects.get(course_name__exact=std_course).id
        students_id = Student.objects.get(name__exact=std_name).id
        serializer = PostStdStatusSerializer(
            data={"courses": courses_id,"students": students_id, **request.data},
            context={"std_name":std_name,"std_course": std_course}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def get_set_std_grade(request):
    if request.method == 'GET':
        return Response('尚未實作')
    elif request.method == 'POST':
        if not request.auth:
            return Response('沒有權限')
        else:
            content = {'auth': str(request.auth),'user':str(request.user)}
            return Response(content)

@api_view(['GET'])
@permission_classes([CustomPermission])
def see_after_login(request):
    return Response("確認登入才看的到我")