from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phone_field import PhoneField

# Create your models here.
class GenderChoice(models.TextChoices):
    MALE = u'M', 'Male'
    FEMALE = u'F', 'Female'
    OTHERS = u'O', 'Other'


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self,username, email, first_name= None, last_name= None, password = None):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
        )        
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,username,email, password):
        """
        Create and save a SuperUser with the given email and password.
        """
        user = self.create_user(
            username = username,
            email = email,
            password = password,
        )        
        user.user_administrator = True
        user.save()
        return user

# Create your models here.
class Profile(models.Model):
    username = models.CharField('Username', unique = True,max_lenght = 100,blank=True,null=True)
    first_name = models.CharField('First Name',max_length = 100,null = False, blank = False)
    last_name = models.CharField('Last Name', max_length = 200,null = False, blank = False)
    email = models.EmailField('Email',null = False,unique = True, blank = False)
    password = models.CharField('Password',max_length=10, null = False, blank = False)
    user_active = models.BooleanField('Active',null = False, blank = False)
    user_administrator = models.BooleanField('Active',null = False, blank = False)
    gender = models.CharField('Gener',max_length=2,choices=GenderChoice.choices,default=GenderChoice.OTHERS)
    phone = PhoneField('Phone',max_length=31,blank=True,null=True)
    birthday = models.DateField('Birthday',blank=True,null=True)
    isActive = models.BooleanField('Active',default=True,null = False, blank = False)
    identification = models.CharField('Identification',default=0,max_length=10)
    score = models.IntegerField('Score',null = False, blank = False)
    image_perfil = models.ImageField('Profile Image',upload_to ='images/',blank=True,null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return '{0},{1}'.format(self.first_name,self.last_name)
    
    def has_perm (self,perm, obj = None):
        return True

    def has_module_perms(self, app_label):
        return True

