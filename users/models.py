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

    TEACHER = 'Teacher'
    STUDENT = 'Student'
    ROLE_CHOICES = (
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student')
    )
    role = models.CharField(max_length=10, 
                            choices=ROLE_CHOICES, 
                            null=True)
    
    signed_participant_form = models.BooleanField(default=False)
    signed_photo_form = models.BooleanField(default=False)

    objects = SailUserManager()

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Teacher(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    # REQUIRED FIELDS
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
        return f'{self.user.first_name} {self.user.last_name}'

class Student(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    # REQUIRED FIELDS
    MALE = 'Male'
    FEMALE = 'Female'
    NON_BIN = 'Non_Binary'
    GENDER_ID_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NON_BIN, 'Non-binary')
    )
    gender_identification = models.CharField(max_length=10, 
                                             choices=GENDER_ID_CHOICES, 
                                             default=MALE)

    XS = 'XS'
    S = 'S'
    M = 'M'
    L = 'L'
    XL = 'XL'
    SHIRT_SIZE_CHOICES = (
        (XS, 'Unisex XS'),
        (S, 'Unisex S'),
        (M, 'Unisex M'),
        (L, 'Unisex L'),
        (XL, 'Unisex XL')
    )
    shirt_size = models.CharField(max_length=5, 
                                  choices=SHIRT_SIZE_CHOICES,
                                  default=XS)

    home_city = models.CharField(max_length=50)
    home_zip_code = models.PositiveIntegerField()
    high_school = models.CharField(max_length=50)

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
    
    phone_number = models.PositiveIntegerField()
    parent_name = models.CharField(max_length=100)
    parent_phone_number = models.PositiveIntegerField()
    parent_email = models.EmailField()

    # OPTIONAL FIELDS (specified with blank=True)
    dietary_restrictions = models.CharField(max_length=50, blank=True)
    home_state = models.CharField(max_length=2, blank=True)
    admitted_student = models.BooleanField(blank=True)

    # FOR INTERNAL LOGISTICS
    signed_medical_form = models.BooleanField(blank=True)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

""" This model describes someone who is "interested" (i.e. we will email them with event updates) """
class Follower(models.Model):
    email = models.EmailField()

    P_TEACHER = 'Prospective Teacher'
    P_STUDENT = 'Prospective Student'
    PARENT = 'Parent'
    ROLE_CHOICES = (
        (P_TEACHER, 'Prospective Teacher'),
        (P_STUDENT, 'Prospective Student'),
        (PARENT, 'Parent / Interested Person'),
    )
    role = models.CharField(max_length=20,
                            choices=ROLE_CHOICES,
                            default=P_TEACHER)

    def __str__(self):
        return self.email
