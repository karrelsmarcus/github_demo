"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from project_app import views
from project_app.views import login_page, landing_page, \
    add_courses_page, add_section_page, view_courses_page, \
    view_account_page, add_account_page, edit_account_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_page.as_view()),
    path('home/', landing_page.as_view()),
    path('create/', add_courses_page.as_view()),
    path('createSec/', add_section_page.as_view()),
    path('createAcc/', add_account_page.as_view()),
    path('courses/', view_courses_page.as_view()),
    path('accounts/', view_account_page.as_view()),
    path('edit/', edit_account_page.as_view()),
    path('courses/delete/<int:id>', views.delete_course, name='delete'),
    path('accounts/delete/<int:id>', views.delete_account, name='delete'),
]
