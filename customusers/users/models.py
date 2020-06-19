from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import UserManager
# Create your models here.


# class Users(AbstractBaseUser, PermissionsMixin):
#     REQUIRED_FIELDS = ('email',)
#     USERNAME_FIELD = 'user_id'
#     user_id = models.IntegerField(primary_key= True)
#     first_name = models.CharField(max_length= 100)
#     last_name = models.CharField(max_length= 100)
#     email  = models.CharField(max_length= 100)
#     password = models.CharField(max_length= 500)
#     objects = UserManager()
#
#     def __str__(self):
#         return  str(self.user_id)

from .managers import CustomUserManager





class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_('email address'), unique=True)
#     is_role = models.IntegerField()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     objects = CustomUserManager()
#
#     def __str__(self):
#         return self.email