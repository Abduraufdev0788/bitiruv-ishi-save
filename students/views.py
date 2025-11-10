from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Student

def add_student(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        new_student = Student(
            first_name = request.POST.get("first_name"),
            last_name = request.POST.get("last_name"),
            faculty = request.POST.get("faculty"),
            group_name = request.POST.get("group_name"),
            theme_name = request.POST.get("theme_name"),
            years = request.POST.get("years"),
            files = request.FILES.get("files"),
        )
        new_student.save()
        return redirect("list_students")
    return render(request, "add_table.html")
