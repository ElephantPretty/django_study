from django.db import models

# Create your models here.
from django.db.models import IntegerField, EmailField


class Book(models.Model):
    title = models.CharField(verbose_name='书名', max_length=50, default='', unique=True)
    #默认django新添字段是null=False,即非空
    pub = models.CharField('出版社', max_length=100, default='')
    price = models.DecimalField('图书定价', max_digits=7, decimal_places=2)
    market_price = models.DecimalField('图书零售价', max_digits=7, decimal_places=2,default=0.0)
    # mysql里面是tinyint
    is_active = models.BooleanField('是否活跃', default=True)
    class Meta:
        db_table = 'book'
        verbose_name = '图书'
        verbose_name_plural = verbose_name
    def __str__(self):
        return '%s_%s_%s_%s'%(self.title, self.pub, self.price,
                              self.market_price)


class Author(models.Model):
    name = models.CharField('姓名', max_length=11, default='张三', unique=True)
    age = IntegerField('年龄', default=1)
    # 允许为空
    email = EmailField('邮箱', null=True)
    class Meta:
        db_table = 'author'

