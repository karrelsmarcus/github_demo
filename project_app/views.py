from django.shortcuts import render, redirect
from django.views import View
from .models import *


class login_page(View):
    def get(self, request):
        return render(request, "loginPage.html", {})

    def post(self, request):
        # this is for bypassing the log in
         return redirect("/home/")
        # name = request.POST['name']
        # password = request.POST['password']
        #
        # valid = self.validate_login(name, password)
        #
        # if valid:
        #     request.session["name"] = name
        #     return redirect("/home/")
        # else:
        #     return render(request, "loginPage.html", {"message": "invalid login credentials"})

    def validate_login(self, user_name, password):
        # no_user = False
        # bad_password = False
        # try:
        #     u = supervisor.objects.get(name=user_name)
        #     bad_password = (u.password != password)
        # except:
        #     no_user = True
        # if no_user or bad_password:
        #     return False
        # else:
        #     return True

        # this is for bypassing the log in
        pass


class landing_page(View):

    options = {"0": "landingPage.html",
               "1": "landingPage_instructor.html"}

    def get(self, request):
        # u = supervisor.objects.get(name=request.session["name"])
        # return render(request, self.options.get(u.user_id), {})

        # this is for bypassing the log in
        return render(request,"landingPage.html", {})

    def post(self, request):
        # u = supervisor.objects.get(name=request.POST['name'])
        # p = supervisor.objects.get(password=request.POST['password'])
        # return redirect("/home/")

        # this is for bypassing the log in
        pass



class courses_page(View):
    def get(self, request):
        return render(request, "viewCourse.html", {})

    def post(self, request):
        pass

class add_courses_page(View):
    def get(self, request):
        return render(request, "addCourse.html", {})

    def post(self, request):
        pass

    def get_courses(self, user_name):
        pass

    def create_course(self, course_name, section, number, inst):
        pass

    def assign_instructor(self, section, inst):
        pass

