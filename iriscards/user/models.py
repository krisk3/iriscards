"""
Database models.
"""
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

class UserManager(BaseUserManager):
    """Manager for users."""
    def create_user(self, email, password, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        if not password:
            raise ValueError('User must have a password.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class FirstPassword(models.Model):
    """
    Model to store the default password for the user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "First Password"
        verbose_name_plural = "First Password"

    def __str__(self):
        """
        Return a string representation of the F password.

        Returns:
        - str: Password.
        """
        return f"{self.user.email} - {self.password}"