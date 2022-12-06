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
        u = supervisor.objects.get(name=request.session["name"])
        courses = self.get_courses(u)
        return render(request, self.options.get(u.user_id), {"courses": courses})

    def post(self, request):
        resp = request.POST.get("create")
        print(resp)
        if resp != '':
            return render(request, 'addCourse.html', {})

    def get_courses(self, user_name):
        return list(map(str, course.objects.filter(owner__name=user_name)))





class add_courses_page(View):
    def get(self, request):

        # name = str(request.GET["cname"])
        # ncourse = int(request.GET["cnum"])
        # section = int(request.GET["snum"])

        return render(request, "addCourse.html", {})

    def post(self, request):

        sup = request.session["name"]
        resp = request.POST.get("Add Course")
        resp1 = request.POST.get("bbutton")
        if resp != '':
            self.create_course(request.POST.get("cname"), request.POST.get("cnum"), request.POST.get("snum"), None, sup)
            courses = list(map(str, course.objects.filter(owner__name=sup)))

        if resp1 != '':
            return render(request, "landingPage.html", {})
        else:
            return render(request, "addCourse.html", {})

    def create_course(self, course_name, number, section, inst, owner):
        new_course = course(name=course_name, number=number, section=section,
                            instructor=inst, owner=supervisor.objects.get(name=owner))
        new_course.save()

    def assign_instructor(self, section, inst):
        pass
