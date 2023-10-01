from dataclasses import field
from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["name","gender","age","school","hobby"]

class CoursesInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursesInfo
        fields = ["course_name","difficulty"]

class StdCourseStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StdCourseStatus
        fields = ["courses","students","data_start","status"]

class PostStdStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StdCourseStatus
        fields = ["data_start","status"]

    def to_representation(self):
        return {
            "std_name":self.context["std_course"],
            "std_course":self.context["std_name"],
            **self.validated_data
        }

    def create(self, validated_data):
        course = self.context["std_course"]
        student = self.context["std_name"]

        course_dict = CoursesInfo.objects.get(course_name__exact=course)
        student_dict = Student.objects.get(name__exact=student)

        return StdCourseStatus.objects.create(courses=course_dict,students=student_dict,**validated_data)
