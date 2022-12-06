from django.db import models

# user_id: supervisor = 0
#          instructor = 1


class MyUser(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user_id = models.CharField(max_length=1)


class course(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=3)
    section = models.CharField(max_length=3)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
