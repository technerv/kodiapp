import uuid
from datetime import timedelta
# from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Permission

class MyUserManager(BaseUserManager):
    
    def _create_user(self, email, password, salutation, first_name, middle_name, last_name, mobile_number, is_owner, is_tenant, is_staff, is_superuser, **extra_fields):
        """
        Create and save User credentials.

        :param email: string
        :param password: string
        :param first_name: string
        :param last_name: string
        :param is_owner: boolean
        :param is_tenant: boolean
        :param is_staff: boolean
        :param is_superuser: boolean
        :param extra_fields:
        :return: User
        """
        now = timezone.now()
        
        email = self.normalize_email(email)
        
        user = self.model(email=email,
                          salutation=salutation,
                          first_name=first_name,
                          last_name=last_name,
                          middle_name=middle_name,
                          is_owner=is_owner,
                          is_tenant=is_tenant,
                          is_staff=is_staff,
                          is_active=True,
                          mobile_number=mobile_number,
                          is_superuser=is_superuser,
                          last_login=now,
                          date_joined=now, **extra_fields)
        
        user.set_password(password)
        
        user.save(using=self._db)

        return user

    def create_user(self, email, first_name, last_name, password, **extra_fields):
        """
        Create and save an User with the given email, password and name.

        :param email: string
        :param first_name: string
        :param last_name: string
        :param password: string
        :param extra_fields:
        :return: User
        """

        return self._create_user(email, password, first_name, last_name, is_owner=False, is_tenant=False, is_staff=False, is_superuser=False,
                                 **extra_fields)

    def create_superuser(self, email, salutation='', first_name='', mobile_number='0722471224', middle_name='', last_name='', password=None, **extra_fields):
        """
        Create a super user.

        :param email: string
        :param first_name: string
        :param last_name: string
        :param password: string
        :param extra_fields:
        :return: User
        """
        return self._create_user(email, password, salutation, first_name, middle_name,last_name, mobile_number, is_staff=True, is_superuser=True, 
                                 **extra_fields)

# We have overrided the Abstact User Class and created 
# our own custom user model to use
class User(AbstractBaseUser, PermissionsMixin,):
    """
    Model that represents an user.

    To be active, the user must register and confirm his email.
    """
    # CHOICE OF GENDER
    GENDER_MALE = 'MR'
    GENDER_FEMALE = 'MRS'
    GENDER_FEMALE_NOTMARRIED = 'MISS'
    GENDER_MARRIED = (
        (GENDER_MALE, 'MR'),
        (GENDER_FEMALE, 'MRS'),
        (GENDER_FEMALE_NOTMARRIED, 'MISS')
    )

    GENDER_MALE = 'Male'
    GENDER_FEMALE = 'Female'
    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female')
    )

    # we want primary key to be called id so need to ignore pytlint
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)   
    
    # Main fields that contain user information
    salutation = models.CharField(_('Salutation'), choices = GENDER_MARRIED, max_length=8)
    first_name = models.CharField(_('First Name'), max_length=50)
    middle_name = models.CharField(_('Middle Name'), max_length=50, blank=True, null=True)
    last_name = models.CharField(_('Last Name'), max_length=50)    
    email = models.EmailField(_('Email address'), unique=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    confirmed_email = models.BooleanField(default=False)
    mobile_number = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to="img", blank=True)

    # Type of Profile (Tenant/Owner)
    is_owner = models.BooleanField(_('Plot/Land Owner'), default=False)
    is_tenant = models.BooleanField(_('Tenant'), default=False)
    
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_superuser = models.BooleanField(_('superuser status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)

    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    date_updated = models.DateTimeField(_('date updated'), auto_now=True)
    activation_key = models.UUIDField(unique=True, default=uuid.uuid4)  # email

    USERNAME_FIELD = 'email' # Set email instead of username to be the default login field

    objects = MyUserManager()

    class Meta:
        
        ordering = ('-date_updated',)
        # permissions = (
        #             ("view_user", "Can view user"),
        #         )
    def __str__(self):
        
        """
        Unicode representation for an user model.

        :return: string
        """
        return self.email

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.

        :return: string
        """
        return "{0} {1}".format(self.first_name, self.last_name)

    def get_short_name(self):
        """
        Return the first_name.

        :return: string
        """
        return self.first_name
    
    def get_mobile_number(self):
        """
        Return the first_name.

        :return: string
        """
        return self.mobile_number
    
    def activation_expired(self):
        """
        Check if user's activation has expired.

        :return: boolean
        """
        return self.date_joined + timedelta(days=7) < timezone.now()

    def confirm_email(self):
        """
        Confirm email.

        :return: boolean
        """
        if not self.activation_expired() and not self.confirmed_email:
            self.confirmed_email = True
            self.save()
            return True
        return False
    
    def get_userid(self):
        return self.id

    def get_groups(self):
        
        return self.groups.values_list('name',flat=True);
    
    def get_all_permissions(self):
        
        self.refresh_from_db()
        return self.user_permissions.all().values_list('codename', flat=True) | Permission.objects.filter(group__user=self).values_list('codename', flat=True);
