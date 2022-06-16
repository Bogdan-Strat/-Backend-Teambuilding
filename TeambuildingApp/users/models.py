from django.db import models
from django.contrib.auth.models import User

'''
class Lead(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=100, unique=True)
  message = models.CharField(max_length=100, blank=True)
  owner = models.ForeignKey(User, related_name="leads", on_delete=models.CASCADE, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
'''
class Activity(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)

    class Meta:
        app_label = 'users'

class Team(models.Model):
    name = models.CharField(max_length=50)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True)

    class Meta:
        app_label = 'users'

class Details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=None)
    company_name = models.CharField(max_length=50)

    class Meta:
        app_label = 'users'

class Member(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(Details, on_delete=models.CASCADE, null=True)

    class Meta:
        app_label = 'users'
        unique_together = ('team','user')