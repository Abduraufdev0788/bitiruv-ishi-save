from django.views import View
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from random import randint

from .models import Registration


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


        return render(request, "verify.html")
    

class VerifyEmail(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "verify.html")

    def post(self, request: HttpRequest) -> HttpResponse:
        input_code = request.POST.get("code")
        session_code = str(request.session.get("verification_code"))

        if input_code != session_code:
            return render(request, "verify.html", {"error": "Kod notogri!"})


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

        return render(request, "login.html")
