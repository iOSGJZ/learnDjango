"""learnDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url,include
from blog import views
from rest_framework import routers
from quickstart import views as apiView
"""
urlpatterns = [
    path(正则表达式, views视图函数，参数，别名),
]
参数说明：
1、一个正则表达式字符串
2、一个可调用对象，通常为一个视图函数或一个指定视图函数路径的字符串
3、可选的要传递给视图函数的默认参数（字典形式）
4、一个可选的name参数(别名)
"""

router = routers.DefaultRouter()
router.register(r'users',apiView.UserViewSet)
router.register(r'groups',apiView.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.hello),
    path('',views.index, name = 'index'),
    path('orm/',views.orm),
    url(r'^',include(router.urls)),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    url(r'^',include('snippets.urls')),

]
