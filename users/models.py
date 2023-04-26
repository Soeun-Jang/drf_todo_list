from django.db import models
from django.contrib.auth.models import ( 
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        #주어진 개인정보로 인스턴스 생성
        
        if not email:
          raise ValueError("회원가입 시 이메일이 필요합니다.")
        user = self.model(
          email=self.normalize_email(email),
          **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email=None, password=None):
        superuser = self.create_user(
            email=email,
            password=password,
        )
        superuser.is_superuser = True
        superuser.is_admin = True      
        superuser.save(using=self._db)
        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name= _('Email address'),
        max_length= 50,
        unique=True
      )
    username = models.CharField(
        verbose_name= _('Username'),
        max_length=30,
        unique=False
      )
    age = models.PositiveIntegerField(
        verbose_name= _('Age'),
        default=0  
    )

    genders = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    
    gender = models.CharField(
        verbose_name= _('Gender'),
        choices=genders,
        max_length=6
    )
    
    introduction = models.CharField(
        verbose_name= _('Introduce Myself'),
        max_length=255
    )
    
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin