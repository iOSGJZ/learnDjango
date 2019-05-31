from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField('分类',max_length=100)
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField('标签',max_length = 100)
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('标题',max_length=70)
    intro = models.TextField('摘要',max_length=200,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='分类',default='1')
    tags = models.ManyToManyField(Tags, blank=True, verbose_name='标签')
    body = models.TextField('内容',max_length=200,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者',default=1)
    created_time = models.DateTimeField('发布时间',auto_now_add=True)

    #只是Django的内部类，属于模型的嵌套类,用于定义模型的一些特征
    #verbose_name用于给模型起一个可读性更好的名字，verbose_name_plural是复数名字，如不定义则会自动加上s
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title