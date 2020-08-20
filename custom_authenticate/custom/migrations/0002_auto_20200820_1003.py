# Generated by Django 3.1 on 2020-08-20 15:03

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('custom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Username')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=200, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('password', models.CharField(max_length=10, verbose_name='Password')),
                ('user_active', models.BooleanField(verbose_name='Active')),
                ('user_administrator', models.BooleanField(verbose_name='Active')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='O', max_length=2, verbose_name='Gener')),
                ('phone', phone_field.models.PhoneField(blank=True, max_length=31, null=True, verbose_name='Phone')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Birthday')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_staff', models.BooleanField(default=True, verbose_name='Staff')),
                ('identification', models.CharField(default=0, max_length=10, verbose_name='Identification')),
                ('score', models.IntegerField(verbose_name='Score')),
                ('image_perfil', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Profile Image')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]