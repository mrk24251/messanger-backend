from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Massanger(models.Model):
    username = models.CharField(max_length=200,blank=False)
    password = models.CharField(max_length=50,blank=False)
    first_name=models.CharField(max_length=100,blank=True, default="")
    last_name=models.CharField(max_length=100,blank=True, default="")
    city = models.CharField(max_length=100, blank=True, default="")
    bio = models.CharField(max_length=500, blank=True, default="")
    query = models.CharField(max_length=500, blank=False, default="")
    messages = models.CharField(max_length=500, blank=True)
    create_at=models.DateTimeField(auto_now_add=True)

class ConversationList(models.Model):
    username = models.CharField(max_length=200,blank=False,null=True)
    first_name=models.CharField(max_length=100,blank=True, default="",null=True)
    last_name=models.CharField(max_length=100,blank=True, default="",null=True)
    create_at=models.DateTimeField(auto_now_add=True,null=True)
    owner = models.ForeignKey(Massanger, related_name='Messanger', on_delete=models.CASCADE,null=True)
    user_id=models.IntegerField(null=True)
    # user_id = models.IntegerField(default=1)