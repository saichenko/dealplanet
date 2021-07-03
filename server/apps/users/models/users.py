from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from datetime import date
from django.forms import ValidationError


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address.')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def birt_date_validator(value):
    if value > date(year=date.today().year - 5, month=1, day=1):
        raise ValidationError('Birth date is invalid')
    return value


class User(AbstractBaseUser):
    email = models.EmailField(max_length=60, unique=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    birth_date = models.DateField(
        verbose_name='день рождения',
        blank=True,
        null=True,
        validators=[birt_date_validator]
    )

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
