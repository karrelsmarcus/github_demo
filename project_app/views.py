from django.shortcuts import render, redirect
from django.views import View
from .models import supervisor, instructor, course


# Create your views here.
class login_page(View):
    def get(self, request):
        return render(request, "loginPage.html", {})

    def post(self, request):
        pass


class landing_page(View):
    def get(self, request):
        return render(request, 'landingPage.html', {})

    def post(self, request):
        pass


class courses_page(View):
    def get(self, request):
        return render(request, 'loginPage.html', {})

    def post(self, request):
        pass
