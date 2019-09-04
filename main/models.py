from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from djmoney.models.fields import MoneyField

# Create your models here.

class UserManager(BaseUserManager):
    use_in_migration=True

    def _create_user(self,email,password,**extra_fields):
        """
        Event manager user creation methods
        """
        if not email:
            raise ValueError('The given email must be set')

        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_superuser',False)
        extra_fields.setdefault('is_staff',False)
        return self._create_user(email,password,**extra_fields)

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_staff',True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(email,password,**extra_fields)




class User(AbstractBaseUser, PermissionsMixin):

    email=models.EmailField(_('email address'),unique=True)
    full_name=models.CharField(_('full name'), max_length=200,blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    phone=models.CharField(_('phone number'),max_length=20,blank=True,null=True)
    balance=MoneyField(max_digits=10,decimal_places=2,default=0,default_currency='XOF')
    is_staff=models.BooleanField(_('staff member'), default=False)

    objects=UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    class Meta:
        verbose_name=_('user')
        verbose_name_plural=_('users')
