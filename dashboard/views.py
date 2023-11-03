from django.shortcuts import render
from django.views.generic import TemplateView, View


class DashboardView(TemplateView):
    template_name = "dashboard/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = None
        return context


class DashboardSettingsView(TemplateView):
    template_name = "dashboard/settings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = None
        return context


class DashboardUpdateView(TemplateView):
    template_name = "dashboard/update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = None
        return context


class DashboardReviewView(TemplateView):
    template_name = "dashboard/reviews.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = None
        return context
