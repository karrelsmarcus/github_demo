from django.db import models

# user_id: supervisor = 0
#          instructor = 1


class supervisor(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user_id = models.CharField(max_length=1)


class instructor(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class course(models.Model):
    supervisor = models.ForeignKey(supervisor, on_delete=models.CASCADE)
    instructor = models.ForeignKey(instructor, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=3)
    section = models.CharField(max_length=3)
