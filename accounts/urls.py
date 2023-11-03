from django.urls import path
from .views import LoginView, ProfileView, RegisterView, OtpView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("otp/", OtpView.as_view(), name="otp"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
