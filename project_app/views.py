from django.shortcuts import render, redirect
from django.views import View
from .models import supervisor, instructor, course


# Create your views here.
class login_page(View):
    def get(self, request):
        return render(request, "loginPage.html", {})

    def post(self, request):
        return redirect('/home/')


class landing_page(View):
    def get(self, request):
        return render(request, "landingPage.html", {})

    def post(self, request):
        # u = supervisor.objects.get(name=request.POST['name'])
        # p = supervisor.objects.get(password=request.POST['password'])
        # return redirect("/home/")
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
