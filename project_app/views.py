from django.shortcuts import render, redirect
from django.views import View
from .models import *
from . import account_methods as am, course_methods as cm, validations as v


class page(View):

    def get(self, request):
        pass

    def post(self, request):
        pass


class login_page(page):
    def get(self, request):
        return render(request, "loginPage.html", {})

    def post(self, request):
        name = request.POST['name']
        password = request.POST['password']

        valid = v.validation.validate_login(v.validation(), name, password)

        if valid:
            request.session["name"] = name
            return redirect("/home/")
        else:
            return render(request, "loginPage.html", {"message": "invalid login credentials"})
        # return render(request,'landingPage.html', {})


class landing_page(page):
    options = {MyUser.SUP: "landingPage.html",
               MyUser.INS: "landingPage_instructor.html"}

    def get(self, request):
        u = MyUser.objects.get(user_name=request.session['name'])
        return render(request, "landingPage.html", {'name': u.get_name(), 'role': u.get_permission(),
                                                    'address': u.get_address(), 'phone': u.get_phone(),
                                                    'email': u.get_email()})

    def post(self, request):
        resp = request.POST.get("view_courses")
        resp1 = request.POST.get("logout")
        resp2 = request.POST.get("view_accounts")
        resp3 = request.POST.get("edit_profile")
        u = MyUser.objects.get(user_name=request.session['name'])

        if resp1:
            return render(request, 'loginPage.html', {})

        if resp2:
            return redirect("/accounts/")

        if resp3:
            return redirect("/edit/")

        if resp:
            return redirect("/courses/")


class edit_account_page(page):

    def get(self, request):
        u = MyUser.objects.get(user_name=request.session['name'])
        return render(request, "editAccount.html", {'name': u.user_name})

    def post(self, request):
        resp = request.POST.get("back")
        resp1 = request.POST.get("confirm")

        if resp1:
            u = MyUser.objects.get(user_name=request.session['name'])
            e = request.POST.get("email")
            p = request.POST.get("pnum")
            a = request.POST.get("addr")
            am.account_methods.edit_account(am.account_methods(), e, p, a, u)
            return redirect("/home/")

        if resp:
            return redirect("/home/")


class view_courses_page(page):

    def get(self, request):
        u = MyUser.objects.get(user_name=request.session['name'])
        courses = cm.course_methods.get_courses_user(cm.course_methods(), u)
        return render(request, 'viewCourse.html', {"courses": courses})

    def post(self, request):
        u = MyUser.objects.get(user_name=request.session['name'])
        resp0 = request.POST.get("create_course")
        resp = request.POST.get("create_section")
        resp1 = request.POST.get("back")

        if resp1:
            return redirect("/home/")

        if resp:
            return redirect("/createSec/")

        if resp0:
            return redirect("/create/")


class add_courses_page(View):
    def get(self, request):
        u = MyUser.objects.get(user_name=request.session['name'])
        return render(request, "addCourse.html", {"name": u.user_name})

    def post(self, request):
        sup = MyUser.objects.get(user_name=request.session["name"])
        print(sup.user_name)
        resp = request.POST.get("add_course")
        resp1 = request.POST.get("back")

        if resp:
            cm.course_methods.create_course(cm.course_methods(), request.POST.get("cname"),
                                                request.POST.get("cnum"), sup)

        if resp1:
            return redirect("/courses/")

        return render(request, "addCourse.html", {"name": sup.user_name})


class add_section_page(page):
    def get(self, request):
        accounts = am.account_methods.get_accounts(am.account_methods())
        courses = cm.course_methods.get_courses_all(cm.course_methods())
        return render(request, "addSection.html",
                      {'name': request.session['name'], 'accounts': accounts, 'courses': courses})

    def post(self, request):

        resp = request.POST.get("back")
        resp1 = request.POST.get("add")

        if resp:
            return redirect("/courses/")

        if resp1:
            c = course.objects.get(name=request.POST.get("course"))
            a = MyUser.objects.get(user_name=request.POST.get("account"))
            n = request.POST.get("snum")
            s = request.POST.get("stime")
            e = request.POST.get("etime")

            cm.course_methods.create_section(cm.course_methods(), c, a, n, s, e)
            return redirect("/createSec/")

        return redirect(request, "addSection.html", {'message': 'error adding section'})


class view_account_page(page):

    def get(self, request):
        u = MyUser.objects.get(user_name=request.session["name"])
        a = am.account_methods.get_accounts(am.account_methods())
        return render(request, "viewAccounts.html", {'name': u.user_name, 'accounts': a})

    def post(self, request):
        resp = request.POST.get("create_accounts")
        resp1 = request.POST.get("back")

        if resp:
            return redirect("/createAcc/")
        if resp1:
            return redirect("/home/")


class add_account_page(page):
    def get(self, request):

        return render(request, 'createAccount.html', {"permission_choice": MyUser.user_permission})

    def post(self, request):
        sup = MyUser.objects.get(user_name=request.session["name"])
        resp = request.POST.get("submit")
        resp1 = request.POST.get("back")

        if resp:
            user_name = request.POST.get("user_name")
            pw = request.POST.get("password")
            pw1 = request.POST.get("password1")
            perm = request.POST.get("permission")
            f_name = request.POST.get("first_name")
            l_name = request.POST.get("last_name")
            am.account_methods.create_account(am.account_methods(), user_name, pw, pw1, perm, f_name, l_name)
            return redirect("/createAcc/")

        if resp1:
            return redirect("/accounts/")

        return render(request, "createAccount.html", {"message": 'error creating account'})


def delete_course(request, id):
    c = section.objects.get(id=id)
    c.delete()
    return redirect('/courses/')


def delete_account(request, id):
    a = MyUser.objects.get(id=id)
    a.delete()
    return redirect('/accounts/')
