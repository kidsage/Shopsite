from django.db import models
from accounts.models import User
from product.models import Product

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='사용자', related_name='user')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='상품', related_name='product')
    quantity = models.IntegerField(verbose_name='수량')
    created_dt = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.user.profile.nickname

    class Meta:
        db_table = 'order'


# 장바구니 모델 설정 시작
# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
#     product = models.ForeignKey(Producton_delete=models.CASCADE, related_name='product')
#     active = models.BooleanField(default=False)
#     # 수량은 -1 과 같은 수량이 없기 때문에 아래의 필드로 선언하여 최소값을 1 로 설정
#     quantity = models.PositiveSmallIntegerField(null=True, default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
#     created_at = models.DateTimeField(auto_now_add=True)