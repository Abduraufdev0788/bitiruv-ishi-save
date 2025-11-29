from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
from .models import Registration
from django.contrib.auth.hashers import make_password


class Register(View):
    def get(self, request:HttpRequest)->HttpResponse:
        return render(request=request, template_name="register.html")
    
    def post(self, request:HttpRequest)->HttpResponse:
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if not name:
            return JsonResponse({"message": "name required"}, status = 401)
        
        if len(name)>200 or len(name)<3:
            return JsonResponse({"message": "min length 3 max length 200 characters"}, status = 401)
        
        if not surname:
            return JsonResponse({"message": "surname required"}, status = 401)
        
        if len(surname)>200 or len(surname)<3:
            return JsonResponse({"message": "min length 3 max length 200 characters"}, status = 401)
        
        if not email:
            return JsonResponse({"message": "email required"}, status  =401)
        
        if not password:
            return JsonResponse({"message":"password required"}, status = 401)
        if len(password) > 256:
            return JsonResponse({"message": "password max 256 characters"}, status = 401)
        
        if confirm_password != password:
            return JsonResponse({"message": "password must be the same"})
        
        new_user = Registration(
            name = name,
            surname = surname,
            email = email,
            password = make_password(password = password)
        )
        new_user.save()

        request.session['user_id'] = new_user.id
        


        return JsonResponse({"royxatdan":"doiferm"})