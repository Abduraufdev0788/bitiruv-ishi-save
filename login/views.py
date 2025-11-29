from django.views import View
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from random import randint

from .models import Registration, Student


class Kirish(View):
    def get(self, request:HttpRequest)->HttpResponse:
        return render(request=request, template_name="index.html")
    
class Login(View):
    def get(self,request:HttpRequest)->HttpResponse:
        return render(request=request, template_name="login_page.html")


class Register(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "register.html")
    
    def post(self, request: HttpRequest) -> HttpResponse:
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

      
        if not name:
            return JsonResponse({"message": "name required"}, status=401)
        if len(name) < 3 or len(name) > 200:
            return JsonResponse({"message": "name: min 3, max 200 characters"}, status=401)

        if not surname:
            return JsonResponse({"message": "surname required"}, status=401)
        if len(surname) < 3 or len(surname) > 200:
            return JsonResponse({"message": "surname: min 3, max 200 characters"}, status=401)

        if not email:
            return JsonResponse({"message": "email required"}, status=401)
        if Registration.objects.filter(email=email).exists():
            return JsonResponse({"message": "email already exists"}, status=401)

        if not password:
            return JsonResponse({"message": "password required"}, status=401)
        if len(password) > 256:
            return JsonResponse({"message": "password max 256 characters"}, status=401)

        if confirm_password != password:
            return JsonResponse({"message": "passwords must match"}, status=401)

 
        request.session['name'] = name
        request.session['surname'] = surname
        request.session['email'] = email
        request.session['password'] = make_password(password)

      
        verification_code = randint(100000, 999999)
        send_mail(
            subject="Verification Code",
            message=f"Your verification code is {verification_code}",
            from_email="turkeynumber063@gmail.com",
            recipient_list=[email],
            fail_silently=False,
        )
        request.session['verification_code'] = verification_code


        return redirect("verify")
    

class VerifyEmail(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "verify.html")

    def post(self, request: HttpRequest) -> HttpResponse:
        d1 = request.POST.get("d1")
        d2 = request.POST.get("d2")
        d3 = request.POST.get("d3")
        d4 = request.POST.get("d4")
        d5 = request.POST.get("d5")
        d6 = request.POST.get("d6")
        input_code = f"{d1}{d2}{d3}{d4}{d5}{d6}"
        session_code = str(request.session.get("verification_code"))
        print((input_code, session_code))

        if input_code != session_code:
            return JsonResponse({"error": "Kod notogri!"}, status=401)


        name = request.session.get("name")
        surname = request.session.get("surname")
        email = request.session.get("email")
        password = request.session.get("password")

        new_user = Registration.objects.create(
            name=name,
            surname=surname,
            email=email,
            password=password
        )

    
        request.session['user_id'] = new_user.id

        for key in ["name", "surname", "email", "password", "verification_code"]:
            if key in request.session:
                del request.session[key]

        return redirect("table")
    

class Login(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "login_page.html")

    def post(self, request: HttpRequest) -> HttpResponse:
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email:
            return JsonResponse({"message": "email required"})
        

        if not Registration.objects.filter(email=email).exists():
            return JsonResponse({"message": "email not found"})

        if not password:
            return JsonResponse({"message": "password required"})

        if len(password) > 256:
            return JsonResponse({"message": "max 256 characters"})

        base_user = Registration.objects.get(email=email)

        if not check_password(password, base_user.password):
            return JsonResponse({"message": "incorrect password"})


        request.session['user_id'] = base_user.id

        return redirect("table")

    
class TableView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        user_id = request.session.get('user_id')
        if not user_id:
            return JsonResponse({"message":"login not defound"})
            
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
    
class AddTableView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "add_table.html")
    
    def post(self, request: HttpRequest) -> HttpResponse:
        user_id = request.session.get('user_id')
        if not user_id:
            return JsonResponse({"message":"login not defound"})
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        faculty = request.POST.get("faculty")
        group_name = request.POST.get("group_name")
        theme_name = request.POST.get("theme_name")
        years = request.POST.get("years")
        files = request.FILES.get("files")

        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            faculty=faculty,
            group_name=group_name,
            theme_name=theme_name,
            years=years,
            files=files
        )

        return redirect("table")
    
