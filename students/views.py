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

def list_students(request: HttpRequest) -> HttpResponse:
    students = Student.objects.all().order_by('-id')

    faculty = request.GET.get("faculty")
    group_name = request.GET.get("group_name")
    theme_name = request.GET.get("theme_name")
    years = request.GET.get("years")

    if faculty:
        students = students.filter(faculty__icontains=faculty)
    if group_name:
        students = students.filter(group_name__icontains=group_name)
    if theme_name:
        students = students.filter(theme_name__icontains=theme_name)
    if years:
        students = students.filter(years__icontains=years)

    return render(request, "table_list.html", {"students": students})
