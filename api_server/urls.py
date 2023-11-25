from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('get_all_student/', views.get_all_student),
    path('get_student_detail/<int:id>/', views.get_student_detail),
    path('student_by_age/<int:gt_age>/', views.student_by_age),
    path('get_all_course/', views.get_all_course),
    path('add_std_course/', views.add_std_course),
    path('get_set_std_grade/', views.get_set_std_grade),
    path('see_after_login/', views.see_after_login),
]
