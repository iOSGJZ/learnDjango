"""
开发我们的Web API的第一件事是为我们的Web API提供一种将代码片段实例序列化和反序列化为诸如json之类的表示形式的方式。
我们可以通过声明与Django forms非常相似的序列化器（serializers）来实现
"""
from rest_framework import serializers
from snippets.models import Snippet,LANGUAGE_CHOICES,STYLE_CHOICES

# class SnippetSerializers(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False,allow_blank=True,max_length=100)
#     code = serializers.CharField(style={'base_template':'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES,default='friendly')

#     def create(self,validated_data):
#         """
#         根据提供的验证过的数据创建并返回一个新的"Snippet"实例
#         """
#         return Snippet.objects.create(**validated_data)

#     def update(self,instance,validated_data):
#         """
#         根据提供的验证过的数据更新和返回一个已经存在的"Snippet"实例
#         """
#         instance.title = validated_data.get('title',instance.title)
#         instance.code = validated_data.get('code',instance.code)
#         instance.lineos = validated_data.get('lineos',instance.lineos)
#         instance.language = validated_data.get('language',instance.language)
#         instance.style = validated_data.get('style',instance.style)
#         instance.save()
#         return instance


"""
REST framework包括Serializer类和ModelSerializer类。
使用ModelSerializer类重构我们的序列化类
序列一个非常棒的属性就是可以通过打印序列化器类实例的结构(representation)查看它的所有字段。
ModelSerializer类并不会做任何特别神奇的事情，它们只是创建序列化器类的快捷方式：
一组自动确定的字段
默认简单实现的create()和update()方法。
"""

class SnippetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id','title','code','linenos','language','style')