from django.urls import path
from .views import Register, TableView, VerifyEmail, AddTableView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("register/", Register.as_view(), name="register"),
    path("verify/", VerifyEmail.as_view(), name="verify"),
    path("table/", TableView.as_view(), name="table"),
    path("add_books/", AddTableView.as_view(), name="add_book")
]
