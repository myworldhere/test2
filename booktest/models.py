# coding=utf-8
from django.db import models


# Create your models here.

# 自定义管理器后，系统就不生成默认的objects对象了。
class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)

    def create(self, title, pub_date):
        b = BookInfo()
        b.title = title
        b.pub_date = pub_date
        b.read = 0
        b.comment = 0
        b.isDelete = False
        return b


class BookInfo(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField(db_column='publish_date')
    read = models.IntegerField(default=0)
    comment = models.IntegerField(null=False)
    isDelete = models.BooleanField(default=False)

    # 模型类内部定义Meta类，可以自定义映射表的内容
    class Meta:
        db_table = 'bookinfo'
    # 自定义管理器对象会取消默认的models对象。
    books1 = models.Manager()
    books2 = BookInfoManager()

    def __str__(self):
        return self.title.encode('utf-8')


class HeroInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField(default=False)
    content = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo)


class AreaInfo(models.Model):
    title = models.CharField(max_length=20)
    parent = models.ForeignKey('self', null=True, blank=True)
