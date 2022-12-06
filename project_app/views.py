from django.shortcuts import render, redirect
from django.views import View
from .models import *


class login_page(View):
    def get(self, request):
        return render(request, "loginPage.html", {})

    def post(self, request):
        name = request.POST['name']
        password = request.POST['password']

        valid = self.validate_login(name, password)

        if valid:
            request.session["name"] = name
            return redirect("/home/")
        else:
            return render(request, "loginPage.html", {"message": "invalid login credentials"})

    def validate_login(self, user_name, password):
        no_user = False
        bad_password = False
        try:
            u = MyUser.objects.get(name=user_name)
            bad_password = (u.password != password)
        except:
            no_user = True
        if no_user or bad_password:
            return False
        else:
            return True


class landing_page(View):
    options = {"0": "landingPage.html",
               "1": "landingPage_instructor.html"}

    def get(self, request):
        u = MyUser.objects.get(name=request.session['name'])
        courses = self.get_courses(u)
        return render(request, self.options.get(u.user_id), {"courses": courses})

    def post(self, request):
        resp = request.POST.get("create")
        if resp != '':
            return render(request, 'addCourse.html', {})

    def get_courses(self, user_name):
        courses = list(course.objects.filter(owner=user_name))
        c = []
        for i in courses:
            name = i._meta.get_field('name')
            number = i._meta.get_field('number')
            section = i._meta.get_field('section')
            c.append([name.value_from_object(i), number.value_from_object(i), section.value_from_object(i)])

        return c


class add_courses_page(View):
    def get(self, request):
        return render(request, "addCourse.html", {})

    def post(self, request):
        sup = MyUser.objects.get(name=request.session["name"])
        resp = request.POST.get("Add Course")

        if resp != '':
            self.create_course(request.POST.get("cname"), request.POST.get("cnum"), request.POST.get("snum"), sup)

        return render(request, "addCourse.html", {})

    def create_course(self, course_name, number, section, owner):
        new_course = course(name=course_name, number=number, section=section,
                            owner=owner)
        new_course.save()

class add_section_page(View):
    def get(self, request):
        return render(request, "addSection.html", {})


    def post(self, request):
        pass
        # sup = MyUser.objects.get(name=request.session["name"])
        # resp = request.POST.get("Add Course")
        #
        # if resp != '':
        #     self.create_course(request.POST.get("cname"), request.POST.get("cnum"), request.POST.get("snum"), sup)
        #
        # return render(request, "addCourse.html", {})

    def create_section(self, course_name, number, section, owner):
        pass
        # new_course = course(name=course_name, number=number, section=section,
        #                     owner=owner)
        # new_course.save()