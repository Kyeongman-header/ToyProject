from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.

class Image(models.Model):
    user=models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,)
    title = models.CharField(max_length=100)
    screenshot = models.ImageField(blank=True)
    pub_date=models.DateTimeField(default=timezone.localtime)

    def __str__(self):
        return str(self.title)

class Points(models.Model):
    user=models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,)
    point_one=models.FloatField(default=0, blank=True,null=True)
    point_two=models.FloatField(default=0,blank=True,null=True)
    point_three=models.FloatField(default=0,blank=True,null=True)
    pub_date=models.DateTimeField(default=timezone.localtime)

    def __str__(self):
        return str(self.title)
    
class UserManager(BaseUserManager):
    def create_user(self,username,password=None,**extra_fields):
        user=self.model(
                username=username,
                last_login=timezone.localtime(),
                date_joined=timezone.localtime(),
                **extra_fields
                )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,password,**extra_fields):
        user=self.create_user(username,password=password,**extra_fields)
        user.is_admin=True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser, PermissionsMixin):
    #machine=models.CharField(max_length=20,unique=True)
    #machine=models.ForeignKey(Machine,on_delete=models.SET_DEFAULT,blank=True,null=True,default=None)
    username=models.CharField(primary_key=True,max_length=20,unique=True)
    
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    date_joined=models.DateTimeField(default=timezone.localtime)
    objects=UserManager()
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['password']

    def __str__(self):
        return self.username
    def has_perm(self,perm,obj=None):
        for p in self.get_all_permissions():
            if p == perm:
                return True
        return self.is_admin
    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.is_admin
