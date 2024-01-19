from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager, PermissionsMixin
import logging

logger = logging.getLogger(__name__)

class CustomKarbarManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class karbar(AbstractUser):
    is_professor = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    sid = models.CharField(max_length=10, unique=True, blank=False, null=False, verbose_name="Student/Professor ID", default='1000000000')
    username = models.CharField(max_length=150, unique=True)
    
    objects = CustomKarbarManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

# class karbar(AbstractUser):
#     is_professor = models.BooleanField(default=False)
#     phone_number = models.CharField(max_length=15, blank=True, null=True)
#     date_of_birth = models.DateField(blank=True, null=True)
#     first_name = models.CharField(max_length=50, blank=False, null=False)
#     last_name = models.CharField(max_length=50, blank=False, null=False)
#     sid = models.CharField(max_length=10, unique=True, blank=False, null=False, verbose_name="Student/Professor ID",default='1000000000')
#     username = models.CharField(max_length=150, unique=True)

#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='karbar_groups',
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='karbar_permissions',
#     )

#     def __str__(self):
#         return f"{self.first_name} {self.last_name} ({self.username})"


# class CustomKarbarManager(BaseUserManager):
#     def create_user(self, username, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         fields = [field.name for field in self.model._meta.get_fields() if field.name != 'id']
#         field_values = {field: extra_fields.pop(field, '') for field in fields}
#         user = self.model(
#             username=username,
#             email=email,
#             **field_values,
#             **extra_fields
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(username, email, password, **extra_fields)