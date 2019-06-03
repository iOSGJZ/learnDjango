"""
序列化
在这个例子中我们用到了超链接关系，使用 HyperlinkedModelSerializer。
你还可以使用主键和各种其他关系，但超链接是好的RESTful设计。
"""
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
