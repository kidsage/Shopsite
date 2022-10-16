from datetime import timezone
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from phonenumber_field.formfields import PhoneNumberField


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, email, **extra_fields):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # python manage.py createsuperuser 사용 시 해당 함수가 사용됨
    def create_superuser(self, username, password, email, **extra_fields):
        extra_fields.setdefault("name", "관리자")
        extra_fields.setdefault("birth_of_date", "1992-05-08")
        extra_fields.setdefault("is_terms_of_service", True)
        extra_fields.setdefault("is_privacy_policy", True)
        extra_fields.setdefault("is_receive_marketing_info", False)
        extra_fields.setdefault("is_admin", True)

        super_user  = self.create_user(
            username=username,
            password=password,
            email=email,
            **extra_fields
        )

        return super_user


class User(AbstractBaseUser):

    objects = CustomUserManager()

    email = models.EmailField(        
        max_length=255,      
        unique=True, 
    )

    date_joined = models.DateTimeField(default=timezone.now)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

    is_active = models.BooleanField("계정 활성화 상태", default=True)
    is_admin = models.BooleanField(default=False)
    is_seller = models.BooleanField("판매자", default=False)

    # id field
    USERNAME_FIELD = 'email'

    # user를 생성할 때 입력받을 필드 지정
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    # 로그인 사용자의 특정 테이블의 crud 권한을 설정, perm table의 crud 권한이 들어간다.
    # admin일 경우 항상 True, 비활성 사용자(is_active=False)의 경우 항상 False
    def has_perm(self, perm, obj=None):
        return True

    # 로그인 사용자의 특정 app에 접근 가능 여부를 설정, app_label에는 app 이름이 들어간다.
    # admin일 경우 항상 True, 비활성 사용자(is_active=False)의 경우 항상 False
    def has_module_perms(self, app_label):
        return True

    # admin 권한 설정
    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'user'


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address')
    address = models.CharField("주소", max_length=100)
    zip_code = models.CharField("우편번호", max_length=10)
    address_tag = models.CharField("배송지명", max_length=20)
    name = models.CharField("받는분 성함", max_length=20)

    def __str__(self):
        return f"{self.user.name}님의 배송지 : {self.address_tag}"

    class Meta:
        db_table = 'address'

class Profile(models.Model):

    def user_directory_path(instance, filename):
        # 공식 docs에서 가져옴.
        return f'user_{instance.user.id}/{filename}'
    
    GENDER_CHOICES = (
        ('남', '남자'),
        ('여', '여자'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField("유저 닉네임", max_length=8, unique=True)
    image = models.ImageField("프로필 이미지", upload_to=user_directory_path, null=True)
    gender = models.CharField("성별", max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField("생년월일", null=True)
    phonenumber = PhoneNumberField("전화번호", region='KR', null=True, blank=True) # iso 3166-1 region codes
    introduce = models.CharField("간략한 소개", max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        db_table = 'profile'