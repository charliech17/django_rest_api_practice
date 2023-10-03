from dataclasses import field
from rest_framework import serializers
from .models import *
import copy


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["name","gender","age","school","hobby"]

class CoursesInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursesInfo
        fields = ["course_name","difficulty"]

class StdCourseStatusSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="students.name")
    student_course = serializers.CharField(source="courses.course_name")
    school = serializers.CharField(source="students.school")
    age = serializers.CharField(source="students.age")
    class Meta:
        model = StdCourseStatus
        fields = ["student_name","student_course","school","age","data_start","status"]

class PostStdStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StdCourseStatus
        fields = ["courses","students","data_start","status"]

    def to_representation(self,value):
        input_data = super().to_representation(value)
        copy_input_data = copy.deepcopy(input_data)
        copy_input_data.pop('courses')
        copy_input_data.pop('students')
        return {
            "std_name":self.context["std_course"],
            "std_course":self.context["std_name"],
            **copy_input_data
        }

    def create(self, validated_data):
        return StdCourseStatus.objects.create(**validated_data)
