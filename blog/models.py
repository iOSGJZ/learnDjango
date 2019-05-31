from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField('标题',max_length=70)
    body = models.TextField('内容',max_length=200,blank=True)
    created_time = models.DateTimeField('发布时间')

    #只是Django的内部类，属于模型的嵌套类,用于定义模型的一些特征
    #verbose_name用于给模型起一个可读性更好的名字，verbose_name_plural是复数名字，如不定义则会自动加上s
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title