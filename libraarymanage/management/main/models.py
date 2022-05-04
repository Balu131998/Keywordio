
from django.db import models

from django.contrib.auth.models import AbstractBaseUser

from django.contrib.auth.models import BaseUserManager
from django.conf import settings

User = settings.AUTH_USER_MODEL


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None,*args,**kwargs):
        """create a new user profile"""

        if not email:
            raise ValueError("user most have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)


        user.save(using=self._db)
        #user.UserRole = kwargs.pop('UserRole')
        # user.MobileNo = kwargs.pop('MobileNo')
        return user

    def create_superuser(self, email, name, password):
        """create and save new super user with given dertails"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


#inheritance UserRole

class UserProfile(AbstractBaseUser):
    """ Database model for user system"""


    email = models.EmailField(max_length=233 , unique=True)
    name = models.CharField(max_length=200)



    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        """retrieve full name of user"""
        return self.name

class register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, null=True)
    user_type = models.CharField(max_length=12, null=True)

    def __str__(self):
        return f'{self.user}'
class Book(models.Model):
    Title=models.CharField(max_length=40,null=True, blank=True)
    Author=models.CharField(max_length=40,null=True, blank=True)
    Department=models.CharField(max_length=40 ,null=True, blank=True)
    def __str__(self):
        return self.Title