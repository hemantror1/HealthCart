from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
GENDER_CHOICES = (
    ("MALE","male"),
    ("FEMALE","female"),
    ("OTHERS","others")
)
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    first_name= models.CharField(max_length=15,null=True,blank=True)
    last_name= models.CharField(max_length=15,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    date_of_birth = models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=225,
                            choices=GENDER_CHOICES,null=True,blank=True)
    city= models.CharField(max_length=15,null=True,blank=True)
    state= models.CharField(max_length=15,null=True,blank=True)
    mobile_number=models.IntegerField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    def __str__(self):
        return self.email
    
    @property

    def is_staff(self): 
        return self.is_admin
        
    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):

        return True