from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)


class UserManager(BaseUserManager):
    def create_user(self, email, full_name=None, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(email=self.normalize_email(email), full_name=full_name)
        user.set_password(password)
        user.staff  = is_staff
        user.active = is_active
        user.admin  = is_admin
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, full_name=None, password=None):
        user = self.create_user(email, full_name, password=password, is_staff=True)
        return user

    def create_superuser(self, email, full_name=None, password=None):
        user = self.create_user(email, full_name, password=password, is_staff=True, is_admin=True)
        return user


class User(AbstractBaseUser):
    email       = models.EmailField(unique=True, max_length=255)
    full_name   = models.CharField(max_length=255, blank=True, null=True)
    active      = models.BooleanField(default=True)  # can login
    staff       = models.BooleanField(default=False)  # staff user non superuser
    admin       = models.BooleanField(default=False)
    timestamp   = models.DateTimeField(auto_now_add=True)
    # confirm     = models.BooleanField(default=False)
    # confirm_date     = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'  # username

    REQUIRED_FIELDS = []  # ['full_name'] - python manage.py createsuperuser

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


# Create your models here.
class GuestEmail(models.Model):
    email     = models.EmailField()
    active    = models.BooleanField(default=True)
    update    = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
