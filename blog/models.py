from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#models使用三步
#1.在models.py中新建或者修改model类
#2.运行 python manage.py makemigrations为改动创建迁移记录,
#3.运行 python manage.py migrate, 将操作同步到数据库


class Category(models.Model):
    """
    Django 要求模型必须继承models.Model类。
    Category 只需要一个简单的分类名name 就可以了
    CharField 指定了分类名name的数据类型，Charfield是字符型
    CharField 的max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库
    然后给name设置了一个’分类’的名称
    """
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
    #TextField用来存储大段文本，blank是否允许为空
    title = models.CharField('标题',max_length=70)
    intro = models.TextField('摘要',max_length=200,blank=True)
    #在这里把文章对应的数据库表和分类，标签对应的数据库表关联起来，但是关联形式稍微有点不同
    #规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以使用的是ForeignKey，既一对的关联关系.
    #对于标签，一篇文章可以有多个标签，同一个标签也可以有多篇文章，所以使用的是ManyToManyField，表明这是多对多的关联关系.
    #文章也可以没有标签，所以设置可以为空
    #Django2.0强制foreignKey必须使用on_delete参数
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='分类',default='1')
    tags = models.ManyToManyField(Tags, blank=True, verbose_name='标签')
    body = models.TextField('内容',max_length=200,blank=True)
    #这里的user是从django.contrib.auth.models导入的，是Django内置的应用，专门用于处理网站用户的注册，登录等流程，user是Django已经为我们写好的用户模型
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者',default=1)
    #存储时间，使用DateTimeField字段，添加auto_now_add参数，自动获取添加时间
    created_time = models.DateTimeField('发布时间',auto_now_add=True)

    #只是Django的内部类，属于模型的嵌套类,用于定义模型的一些特征
    #verbose_name用于给模型起一个可读性更好的名字，verbose_name_plural是复数名字，如不定义则会自动加上s
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title


    #将方法作为列
    #列可以是模型字段，也可以是模型方法，要求方法有返回值
    #设置short_description属性，可以设置在admin站点中显示的列名
    #方法列是不能排序的，如果需要排序需要为方法指定排序依据
    def riqi(self):
        return self.created_time.strftime("%b %d %Y %H:%M:%S")
    #设置方法字段在admin中显示的标题
    riqi.short_description = '发布日期'
    #指定排序依据
    riqi.admin_order_field='created_time'

    #无法直接访问关联对象的属性或方法，可以在模型类中封装方法，访问关联对象的成员
    def paixu(self):
        return self.category.name

    paixu.short_description = '分类名称'