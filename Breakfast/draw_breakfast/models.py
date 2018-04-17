from django.db import models
from django.utils.timezone import now
# Create your models here.

class food_cust(models.Model):
    isegg = models.BooleanField(default=True) # 預設有加蛋 有打勾表示不加蛋-5
    isvegetable = models.BooleanField(default=True)# 預設有+菜 有打勾表示不+菜
    issauce = models.BooleanField(default=True)# 預設有醬 有打勾表示不+醬
    isdanishtoast = models.BooleanField(default=False)# 預設牛奶吐司 有打勾表示要丹麥+20
    issu = models.BooleanField(default=False)# 預設蛋餅 有打勾表示要酥抓+15

    def __str__(self):
        return '%s of %s' % (self.name, self.price)

class foodmenu(models.Model):
    name = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=5)
    type = models.IntegerField(default=5) # 1漢堡 2吐司 3蛋餅 4其他點心 5法式吐司

    def __str__(self):
        return '%s of %s' % (self.name, self.price)

# (早餐店都是去冰) 下面3個需要要選一個
class drink_cust(models.Model):
    isice =  models.BooleanField(default=False) # 有打勾表示去冰
    ismid =  models.BooleanField(default=False) # 有打勾表示溫
    ishot =  models.BooleanField(default=False) # 有打勾表示熱


class drinkmenu(models.Model):
    name = models.TextField(null=True, blank=True)
    price_m = models.IntegerField(default=3)
    price_l = models.IntegerField(default=3)
    drinktype = models.IntegerField(default=3)

class final(models.Model):
    name = models.TextField(null=True, blank=True)
    orderinfo = models.TextField(null=True, blank=True)
    everyprice  = models.IntegerField(default=5)
    ordertime = models.DateTimeField(default=now)
    updatetime = models.DateTimeField(default=now)
