from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """ Helps Django work with our custom user model."""

    def create_user(self, username, email, name, matricula, password=None):
        """ Creates a new user profile object."""
        if not username:
            raise ValueError('O campo de username deve ser preenchido.')

        email = self.normalize_email(email)  # Put all caracters to lower case.
        user = self.model(username=username, email=email, name=name, matricula=matricula)  # Create object
        user.set_password(password)  # Encrypt password to a Hash.
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, name, matricula, password):
        """Creates and saves a new superuser with given details."""

        user = self.create_user(username, email, name, matricula, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a user profile inside the system."""
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    matricula = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email', 'matricula']

    def get_username(self):
        """Used to get a users username."""

        return self.username

    def get_full_name(self):
        """Used to get a users full name."""

        return self.name

    def get_short_name(self):
        """Used to get a users short name."""

        return self.name

    def get_matricula(self):
        """Used to get the student id."""

        return self.matricula

    def __str__(self):
        """Django uses this when it needs to convert the object to a string."""

        return self.email
