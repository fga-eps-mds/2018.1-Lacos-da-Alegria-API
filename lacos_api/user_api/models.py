from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.


class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""

    def create_user(self, email, name, password=None, **kwargs):
        """Creates a new user profile object."""

        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            username=username,
            cpf=cpf,
            birth=birth,
            region=region,
            preference=preference,
            howDidYouKnow=howDidYouKnow,
            want_ongs=want_ongs,
            ddd=ddd,
            whatsapp=whatsapp,
            genre=genre
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password, **kwargs):
        """Creates and saves a new superuser with given details."""

        user = self.create_user(
            email,
            name,
            password,
            username,
            cpf,
            birth,
            region,
            preference,
            howDidYouKnow,
            want_ongs,
            ddd,
            whatsapp,
            genre
        )

        # user.is_superuser = True
        # user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Respents a "user profile" inside our system."""
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=32)
    email = models.EmailField(max_length=255, unique=True)
    cpf = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # doctor_name = models.CharField(max_length=255)
    birth = models.DateField()
    region = models.CharField(max_length=30)
    preference = models.CharField(max_length=255)
    ddd = models.IntegerField()
    whatsapp = models.CharField(max_length=255)
    # participate = models.BooleanField()
    address = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    howDidYouKnow = models.CharField(max_length=255)
    # status = models.IntegerField()
    # profile = models.CharField(max_length=255)
    want_ongs = models.BooleanField(default=False)
    # promoted = models.BooleanField(default=False)
    # voluntary_hours = models.IntegerField()
    # created = models.DateField()

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']


class ProfileFeedItem(models.Model):
    """Profile status update."""

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string."""

        return self.status_text

