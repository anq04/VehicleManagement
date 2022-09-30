from .views import (
    AdminSignupView,
    OwnerSignupView,
    DriverSignupView,
    CustomAuthToken,
    Logout,
    getDriver,
)
from django.urls import path, include
from .router import router

urlpatterns = [
    path("signup/owner", OwnerSignupView.as_view(), name="Owner"),
    path("signup/admin", AdminSignupView.as_view(), name="Admin"),
    path("signup/driver", DriverSignupView.as_view(), name="Driver"),
    path("login/", CustomAuthToken.as_view(), name="login"),
    path("access/", include(router.urls)),
    path("logout/", Logout.as_view()),
    path("rented_car/", getDriver, name="car_detail"),
]
