from django.urls import path
from .views import Login, Register, TableView, VerifyEmail, AddTableView, Kirish



urlpatterns = [
    path("", Kirish.as_view(), name="kirish"),
    path("login/", Login.as_view(), name="login"),
    path("register/", Register.as_view(), name="register"),
    path("verify/", VerifyEmail.as_view(), name="verify"),
    path("table/", TableView.as_view(), name="table"),
    path("add_books/", AddTableView.as_view(), name="add_book")
]
