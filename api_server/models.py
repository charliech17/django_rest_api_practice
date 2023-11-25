from pyexpat import model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
gender_choice = (
    ("man","男"),
    ("woman","女")
)

defficulty_choice = (
    ("hard","難"),
    ("medium","中"),
    ("easy","易"),
)

course_status_choice = (
    ("great","非常好"),
    ("soso","普通"),
    ("bad","不好"),
)

class CoursesInfo(models.Model):
    course_name = models.CharField(max_length=20)
    difficulty = models.CharField(max_length=20,choices=defficulty_choice)
    final_grade = models.DecimalField(max_digits=3,decimal_places=2,null=True)

class Student(models.Model):
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=20,choices=gender_choice)
    age = models.IntegerField(validators=[MinValueValidator(10),MaxValueValidator(40)])
    school = models.CharField(max_length=25)
    hobby = models.CharField(max_length=20,blank=True)
    courses = models.ManyToManyField(CoursesInfo,through="StdCourseStatus")

class StdCourseStatus(models.Model):
    courses = models.ForeignKey(CoursesInfo,on_delete=models.CASCADE)
    students = models.ForeignKey(Student,on_delete=models.CASCADE)
    data_start = models.DateField()
    status = models.CharField(max_length=20,choices=course_status_choice)

    class Meta:
        unique_together = ("courses", 'students')


