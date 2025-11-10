from django.urls import path
from .views import add_student, list_students, student_detail

urlpatterns = [
    path('add/', add_student, name='add_student'),
    path('', list_students, name='list_students'),
    path('<int:pk>/', student_detail, name='student_detail'),
]
