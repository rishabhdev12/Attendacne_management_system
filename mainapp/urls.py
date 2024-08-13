from django.urls import path
from . import views

urlpatterns = [
    path('departments/', views.department_list_create, name='department-list-create'),
    path('departments/<int:pk>/', views.department_detail, name='department-detail'),

    path('courses/', views.course_list_create, name='course-list-create'),
    path('courses/<int:pk>/', views.course_detail, name='course-detail'),

    path('users/', views.user_list_create, name='user-list-create'),
    path('users/<int:pk>/', views.user_detail, name='user-detail'),

    path('students/', views.student_list_create, name='student-list-create'),
    path('students/<int:pk>/', views.student_detail, name='student-detail'),

    path('attendance_logs/', views.attendance_log_list_create, name='attendance-log-list-create'),
    path('attendance_logs/<int:pk>/', views.attendance_log_detail, name='attendance-log-detail'),
]
