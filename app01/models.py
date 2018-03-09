from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group

Group.add_to_class('alias', models.CharField(max_length=64,blank=True,null=True))

class UserProfile(AbstractUser):

    nick_name = models.CharField(max_length=50,verbose_name=u"nick name")