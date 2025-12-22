from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View

class HomeWiews(View):
    def get(self, request):
        return render(request=request, template_name="home_page.html")
