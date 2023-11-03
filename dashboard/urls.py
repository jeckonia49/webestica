from django.urls import path
from .views import (
    DashboardView,
    DashboardSettingsView,
    DashboardUpdateView,
    DashboardReviewView,
)

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("settings/", DashboardSettingsView.as_view(), name="settings"),
    path("update/", DashboardUpdateView.as_view(), name="update"),
    path("reviews/", DashboardReviewView.as_view(), name="reviews"),
]
