from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)


class Project(models.Model):
    name = models.CharField(max_length=100)
    cliref = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='project')

# class User(models.Model):
#     name = models.CharField(max_length=100)
#     projref = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='usrref')