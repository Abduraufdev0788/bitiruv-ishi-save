from django.urls import path
from .views import add_student, list_students
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add/', add_student, name='add_student'),
    path('', list_students, name='list_students'),
    # path('<int:pk>/', student_detail, name='student_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
