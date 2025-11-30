from django.urls import path
from .views import Login, Register, TableView, UpdatePassword, VerifyEmail, AddTableView, Kirish, Forgot_password, SendCode



urlpatterns = [
    path("", Kirish.as_view(), name="kirish"),
    path("login/", Login.as_view(), name="login"),
    path("register/", Register.as_view(), name="register"),
    path("forgot_password/", Forgot_password.as_view(), name = "forgot_password"),
    path("send_code/", SendCode.as_view(), name="sendcode"),
    path("update_password/", UpdatePassword.as_view(), name="update_password"),
    path("verify/", VerifyEmail.as_view(), name="verify"),
    path("table/", TableView.as_view(), name="table"),
    path("add_books/", AddTableView.as_view(), name="add_book")
]
