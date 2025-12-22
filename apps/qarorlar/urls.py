from django.urls import path

from .views import HomeWiews

app_name = "home_page"

urlpatterns = [
    path('', HomeWiews.as_view(), name="home_page")
]
