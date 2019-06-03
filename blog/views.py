from django.shortcuts import render
from django.http import HttpResponse
from blog import models
# Create your views here.

def hello(request):
    return HttpResponse('Hello,world')

def index(request):
    blog_index = models.Article.objects.all().order_by('-id')
    print(blog_index)
    print(type(blog_index))
    context = {
        'blog_index':blog_index,
    }
    return render(request, 'index.html',context)

def orm(request):
    #数据库的增删改查
    #增加有三种方式，严格来说，增加数据只有两种：create()方法和save()方法，一般推荐使用第三种方法
    #第一种方式
   # models.Article.objects.create(title='增加标题一', category_id=1, body='增加内容一',user_id=1)
    #第二种方法：添加数据，实例化表类，在实例化里传参数字段和值
  #  obj = models.Article(title='增加标题二',category_id=1,body='增加内容二',user_id=1)
    #写入数据库
    #obj.save()
    #第三种方式:将要写入的数据组合成字典，键为字段 值为数据
  #  dic = {'title':'增加标题三','category_id':'1','body':'增加内容三','user_id':1}
    #添加到数据库，注意字典变量名称一定要价**
  #  models.Article.objects.create(**dic)

    #删除数据,删除id=3的文章
   # title = models.Article.objects.filter(id=3).delete()

    #修改数据update(字段=值)
    title = models.Article.objects.filter(title='增加标题二').update(title='修改的标题二')
    return HttpResponse('orm')
