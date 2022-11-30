from django.shortcuts import render, redirect
from django.views import View
from .models import *


class login_page(View):
    def get(self, request):
        return render(request, "loginPage.html", {})

    def post(self, request):

        name = request.POST['name']
        password = request.POST['password']

        valid = login_page.validate_login(self, name, password)

        if valid:
            request.session["name"] = name
            return redirect("/home/")
        else:
            return render(request, "loginPage.html", {"message": "invalid login credentials"})

    def validate_login(self, user_name, password):
        no_user = False
        bad_password = False
        try:
            u = supervisor.objects.get(name=user_name)
            bad_password = (u.password != password)
        except:
            no_user = True
        if no_user or bad_password:
            return False
        else:
            return True


class landing_page(View):
    def get(self, request):
        return render(request, 'landingPage.html', {})

    def post(self, request):
        pass

    def get_options(self, user_id):
        pass


class courses_page(View):
    def get(self, request):
        return render(request, 'loginPage.html', {})

    def post(self, request):
        pass

    def get_courses(self, user_name):
        pass

    def create_course(self, course_name, section, number, inst):
        pass

    def assign_instructor(self, section, inst):
        pass

