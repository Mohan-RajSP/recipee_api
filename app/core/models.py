from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):

        if not email:
            raise ValueError

        user = self.model(email= self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password):

        if not email:
            raise ValueError

        suser = self.create_user(email=email,password= password)
        suser.is_superuser = True
        suser.is_staff = True
        suser.set_password(password)
        suser.save()
        return suser


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True,)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default= False)

    objects = UserManager()

    USERNAME_FIELD = 'email' #email


# Create your models here.
