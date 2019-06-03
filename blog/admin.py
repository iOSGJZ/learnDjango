from django.contrib import admin
from .models import Article,Tags,Category
# Register your models here.

#修改登录后台管理页面头部显示和页面标题
admin.site.site_header = '郭兢哲'
admin.site.site_title = '郭兢哲的Django管理后台'


#自定义列表操作
def changeTime(self,request,queryset):
    #批量更新created_time字段的值未2019-5-21
    queryset.update(created_time='2019-5-21')

changeTime.short_description = '中文显示自定义的Actions'


class ArticleAdmin(admin.ModelAdmin):
    """
    一般ManyToManyField多对多字段用过滤器
    标题等文本字段用搜索框
    日期时间用分层筛选。
    过滤器如果是外键需要遵循这样的语法：本表字段__外键表要显示的字段。如：“user__user_name”。
    """

    #搜索框，指定标题title作为搜索字段
    search_fields = ['title']
    #右侧栏过滤器和日期筛选
    list_filter = ['user'] #右侧栏过滤器， 按作者进行筛选
    date_hierarchy = 'created_time' #详细时间分层筛选
    #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    #这里的‘riqi’是方法名，显示一列为方法,方法定义为model的类方法
    list_display = ('id','category','title','user','created_time','riqi','paixu')
    #设置哪些字段可以点击进入编辑界面
    list_display_links = ('title','id')
    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50
    #ordering设置默认排序字段，负号表示降序排序
    ordering = ('-created_time',)
    #list_editable 设置默认可编辑字段，在列表里就可以编辑
    list_editable = ['user']
    #fk_fields 设置显示外键字段
    fk_fields = ['category']
    #操作选项的设置
    #是否在列表顶部显示
    actions_on_top = True
    #是否在列表底部显示
    actions_on_bottom = False
    actions = [changeTime,]


class TagsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)

admin.site.register(Article,ArticleAdmin)
admin.site.register(Tags,TagsAdmin)
admin.site.register(Category,CategoryAdmin)