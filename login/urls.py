from django.urls import path
from .views import Register, TableView, VerifyEmail

urlpatterns = [
    path("register/", Register.as_view(), name="register"),
    path("verify/", VerifyEmail.as_view(), name="verify"),
    path("table/", TableView.as_view(), name="table"),
]