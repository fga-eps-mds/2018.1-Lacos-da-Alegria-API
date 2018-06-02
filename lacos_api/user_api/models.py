from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import (RegexValidator, MinLengthValidator, MaxLengthValidator, MinValueValidator,
                                    MaxValueValidator, EmailValidator)

from lacos_api.activity_api.models import Activity


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
            genre=genre,
            role=role
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
            genre,
            role
        )

        # user.is_superuser = True
        # user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin, RegexValidator):
    """Respents a "user profile" inside our system."""
    username = models.CharField(max_length=255, unique=True, validators=[MinLengthValidator(5), MaxLengthValidator(20),
                                RegexValidator(regex='^[a-zA-Z0-9]+([_-]?[a-zA-Z0-9])*$',
                                message='Username must be Alphanumeric', code='invalid_username', flags=None)])
    password = models.CharField(max_length=110, validators=[MinLengthValidator(6), MaxLengthValidator(110)])
    email = models.EmailField(max_length=255, unique=True, validators=[EmailValidator()])
    cpf = models.CharField(max_length=255, unique=True, validators=[MinLengthValidator(11), MaxLengthValidator(11)])
    name = models.CharField(max_length=255, validators=[MinLengthValidator(3), MaxLengthValidator(50),
                            RegexValidator(regex='^[a-zA-Z]+([ ]?[a-zA-Z])*$')])
    # doctor_name = models.CharField(max_length=255)
    birth = models.DateField()
    region = models.CharField(max_length=30, validators=[MaxLengthValidator(30)])
    preference = models.CharField(max_length=255, validators=[MaxLengthValidator(40)])
    ddd = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(99), RegexValidator(
                              regex='((([2,4,6,8,9][1-9])|(2[1,2,4,7,8])|(3[1-8])|(4[1-9])|(5[1-5])|(7[1,3,4,5,7,9])))'
                              )])
    whatsapp = models.CharField(max_length=255, validators=[MinLengthValidator(8), MaxLengthValidator(9)])
    # participate = models.BooleanField()
    address = models.CharField(max_length=255, validators=[MinLengthValidator(5), MaxLengthValidator(80)])
    genre = models.CharField(max_length=255, validators=[MaxLengthValidator(20)])
    howDidYouKnow = models.CharField(max_length=255)
    # status = models.IntegerField()
    # profile = models.CharField(max_length=255)
    want_ongs = models.BooleanField(default=False)
    # promoted = models.BooleanField(default=False)
    # voluntary_hours = models.IntegerField()
    # created = models.DateField()
    activities = models.ManyToManyField(Activity, blank=True)
    role = models.CharField(max_length=255, default='Novato')

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']
