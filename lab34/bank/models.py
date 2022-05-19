from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(verbose_name='email address',max_length=255, unique=True)
    #username = models.CharField(max_length=35, unique=True)
    first_name = models.CharField(max_length=30, verbose_name='First name')
    last_name = models.CharField(max_length=30, verbose_name='Last name')
    passport_numer = models.CharField(max_length=20, verbose_name='Passport number')
    passport_series = models.CharField(max_length=20, verbose_name='Passport series')
    age = models.PositiveIntegerField(default=0, verbose_name='Age')

    #USERNAME_FIELD = 'username'

class Client(models.Model):
    banks = models.ManyToManyField('Bank')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Bank(models.Model):
    name = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=200, unique=True)


class Manager(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class BankApplication(models.Model):
    bank_id=models.IntegerField()
    client_id=models.IntegerField()


