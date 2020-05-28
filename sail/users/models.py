from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

# Credits for UserManager and User 
# to https://www.fomfus.com/articles/how-to-use-email-as-username-for-django-authentication-removing-the-username

class SailUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class SailUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = SailUserManager()

    def __str__(self):
        return f'{self.email} User'

class SailTeacher(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    major = models.CharField(max_length=50)

    FRESHMAN = 'Freshman'
    SOPHOMORE = 'Sophomore'
    JUNIOR = 'Junior'
    SENIOR = 'Senior'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(max_length=10,
                                      choices=YEAR_IN_SCHOOL_CHOICES,
                                      default=FRESHMAN)
    
    def __str__(self):
        return f'{self.user.email} Teacher -- {self.major}'

class SailStudent(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    is_admitted = models.BooleanField()

    FRESHMAN = 'Freshman'
    SOPHOMORE = 'Sophomore'
    JUNIOR = 'Junior'
    SENIOR = 'Senior'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(max_length=10,
                                      choices=YEAR_IN_SCHOOL_CHOICES,
                                      default=FRESHMAN)
