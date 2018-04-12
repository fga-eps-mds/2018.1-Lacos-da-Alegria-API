# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.models import BaseUserManager

# # Create your models here.

# class UserProfileManager(BaseUserManager):
#     """Helps Django work with our custom user model."""

#     def create_user(self, email, name, password=None):
#         """Creates a new user profile object."""

#         if not email:
#             raise ValueError('Users must have an email address.')

#         email = self.normalize_email(email)
#         user = self.model(email=email, name=name)

#         user.set_password(password)
#         user.save(using=self._db)

#         return user

#     def create_superuser(self, email, name, password):
#         """Creates and saves a new superuser with given details."""

#         user = self.create_user(email, name, password)

#         user.is_superuser = True
#         user.is_staff = True

#         user.save(using=self._db)

#         return user


# class UserProfile(AbstractBaseUser, PermissionsMixin):
#     """Respents a "user profile" inside our system."""

#     login = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=32)
#     email = models.EmailField(max_length=255, unique=True)
#     cpf = models.CharField(max_length=255, unique=True)
#     name = models.CharField(max_length=255)
#     doctorName = models.CharField(max_length=255)
#     birth = models.DateField()
#     ddd = models.IntegerField()
#     whatsapp = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     genre = models.CharField(max_length=255)
#     howDidYouKnow = models.CharField(max_length=255)
#     status = models.IntegerField()
#     profile = models.CharField(max_length=255)
#     wantOngs = models.BooleanField(default=False)
#     promoted = models.BooleanField(default=False)
#     voluntaryHours = models.IntegerField()
#     created = models.DateField()
#     observation = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = UserProfileManager()

#     USERNAME_FIELD = 'login'
#     REQUIRED_FIELDS = ['password','email']

#     def getName(self):
#         """Used to get a user name."""

#         return self.name

#     def getLogin(self):
#         """Used to get a user login."""

#         return self.login

#     def __str__(self):
#         """Django uses this when it needs to convert the object to a string"""

#         return self.email


# class ProfileFeedItem(models.Model):
#     """Profile status update."""

#     user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
#     status_text = models.CharField(max_length=255)
#     created_on = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         """Return the model as a string."""

#         return self.status_text


from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""


    def create_user(self, email, name, password=None):
        """Creates a new user profile object."""

        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given details."""

        user = self.create_user(email, name, password)

        # user.is_superuser = True
        # user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Respents a "user profile" inside our system."""
    # login = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=32)
    email = models.EmailField(max_length=255, unique=True)
    # cpf = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # doctor_name = models.CharField(max_length=255)
    # birth = models.DateField()
    # ddd = models.IntegerField()
    # whatsapp = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    # genre = models.CharField(max_length=255)
    # how_did_you_know = models.CharField(max_length=255)
    # status = models.IntegerField()
    # profile = models.CharField(max_length=255)
    # want_ongs = models.BooleanField(default=False)
    # promoted = models.BooleanField(default=False)
    # voluntary_hours = models.IntegerField()
    # created = models.DateField()

    objects = UserProfileManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get a users full name."""

        return self.name

    def get_short_name(self):
        """Used to get a users short name."""

        return self.name

    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""

        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update."""

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string."""

        return self.status_text
