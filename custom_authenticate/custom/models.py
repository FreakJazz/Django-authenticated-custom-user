from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

# Create your models here.
class GenderChoice(models.TextChoices):
    MALE = u'M', 'Male'
    FEMALE = u'F', 'Female'
    OTHERS = u'O', 'Other'

# Create your models here.
class GroupChoice(models.TextChoices):
    ADMIN = u'A', 'Admin'
    MANAGER = u'M', 'Manager'
    DOCTOR = u'D', 'Doctor'
    EMPLOYEE = u'E', 'Employee'

class DeparmentChoice(models.TextChoices):
    FINANCES = u'F', 'Finances'
    CALLCENTER = u'C', 'Call Center'
    RRHH = u'R', 'Recursos Humanos'
    ADMINISTRACION = u'A', 'Administracion'

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user',blank=True)
    gender = models.CharField('Gener',max_length=2,choices=GenderChoice.choices,default=GenderChoice.OTHERS)
    phone = PhoneField('Phone',max_length=31,blank=True,null=True)
    birthday = models.DateField('Birthday',blank=True,null=True)
    isActive = models.BooleanField('Active',null = False, blank = False)
    identification = models.CharField('Identification',max_length=10)
    score = models.IntegerField('Score',null = False, blank = False)
    workArea = models.CharField('Work Area',max_length=2,choices=DeparmentChoice.choices)

    def __str__(self):
        return str(self.pk) + '    ' + self.user.username
