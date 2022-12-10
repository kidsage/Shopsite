from django.db import models
from accounts.models import User

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='사용자', related_name='user')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='상품', related_name='product')
    quantity = models.IntegerField(verbose_name='수량')
    created_dt = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.user.profile.nickname

    class Meta:
        db_table = 'order'


# 장바구니 모델 설정 시작
# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
#     product = models.ForeignKey('')