from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import (RegexValidator, MinLengthValidator, MaxLengthValidator, MinValueValidator,
                                    MaxValueValidator, EmailValidator)


def validate_genre(value):
    if (value == "Masculino") or (value == "Feminino"):
        print("Valid value")
    else:
        raise ValidationError(
            _('Its not valid'),
            params={'value': value})


def validate_region(value):
    regions = ['Águas Claras',
               'Asa Norte',
               'Asa Sul',
               'Brazlândia',
               'Candangolândia',
               'Ceilândia',
               'Cruzeiro',
               'Entorno Saída Norte',
               'Entorno Saída Sul',
               'Estrutural',
               'Fercal',
               'Gama',
               'Guará',
               'Itapoã',
               'Jardim Botânico',
               'Lago Norte',
               'Lago Sul',
               'Núcleo Bandeirante',
               'Paranoá',
               'Park Way',
               'Planaltina',
               'Recanto das Emas',
               'Riacho Fundo',
               'Riacho Fundo 2',
               'Samambaia',
               'Santa Maria',
               'São Sebastião',
               'Sobradinho',
               'Sobradinho 2',
               'Taguatinga',
               'Varjão',
               'Vicente Pires']
    if value in regions:
        print("Valid Value")
    else:
        raise ValidationError(
            _('Its not valid'),
            params={'value': value})


def validate_preference(value):
    hospitals = ['Hospital Regional do Gama',
                 'Hospital Regional de Taguatinga',
                 'Hospital Universitário de Brasília',
                 'Hospital das Forças Armadas',
                 'Hospital Regional de Planaltina',
                 'Hospital Regional de Sobradinho',
                 'Hospital Regional da Asa Norte']
    if value in hospitals:
        print("Valid Value")
    else:
        raise ValidationError(
            _('Its not valid'),
            params={'value': value})


def validate_HDYK(value):
    options = ['Indicação de um amigo',
               'Através de uma rede social',
               'Através de uma palestra',
               'Em uma reportagem na televisão',
               'Outros']
    if value in options:
        print("Valid Value")
    else:
        raise ValidationError(
            _('Its not valid'),
            params={'value': value})


def validate_cpf(value):
    if len(value) != 11:
        raise ValidationError(
            _('Its not valid'),
            params={'value': value})


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
                                RegexValidator(regex='^[a-zA-Z0-9]+([_-]?[a-zA-Z0-9])*$')])
    password = models.CharField(max_length=255, validators=[MinLengthValidator(6), MaxLengthValidator(255)])
    # RegexValidator(regex='^[a-zA-Z0-9]*$')]) Alterar quando o metodo PUT estiver correto
    email = models.EmailField(max_length=255, unique=True, validators=[EmailValidator()])
    cpf = models.CharField(max_length=255, unique=True, validators=[validate_cpf])
    name = models.CharField(max_length=255, validators=[MinLengthValidator(3), MaxLengthValidator(50),
                            RegexValidator(regex='^[a-zA-Z]+([ ]?[a-zA-Z])*$')])
    # doctor_name = models.CharField(max_length=255)
    birth = models.DateField()
    region = models.CharField(max_length=30, validators=[MaxLengthValidator(30), validate_region])
    preference = models.CharField(max_length=255, validators=[MaxLengthValidator(40), validate_preference])
    ddd = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(99), RegexValidator(
                              regex='^((([1,4,6,8,9][1-9])|(2[1,2,4,7,8])|(3[1-8])|(4[1-9])|(5[1-5])|(7[1,3,4,5,7,9])))*$'  # noqa:E731
                              )])
    whatsapp = models.CharField(max_length=255, validators=[MinLengthValidator(8), MaxLengthValidator(9)])
    # participate = models.BooleanField()
    address = models.CharField(max_length=255, validators=[MinLengthValidator(5), MaxLengthValidator(80)])
    genre = models.CharField(max_length=255, validators=[MaxLengthValidator(20), validate_genre])
    howDidYouKnow = models.CharField(max_length=255, validators=[validate_HDYK])
    # status = models.IntegerField()
    # profile = models.CharField(max_length=255)
    want_ongs = models.BooleanField(default=False)
    # promoted = models.BooleanField(default=False)
    # voluntary_hours = models.IntegerField()
    # created = models.DateField()
    role = models.CharField(max_length=255, default='Novato')
    inscrito = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']
