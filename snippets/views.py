# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
from rest_framework import status #返回的状态码，有详细介绍
from rest_framework.decorators import api_view #基于函数视图的@api_view装饰器
from rest_framework.views import APIView #基于类的视图
from rest_framework import mixins #基于mixin类编写视图
from rest_framework import generics
from rest_framework.response import Response #获取未渲染内容的类型，并使用内容协商来确定返回给客户端的正确内容类型
from snippets.models import Snippet
from snippets.serializers import SnippetSerializers,UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions #rest_framework中的权限类，有很多，根据需求使用
# Create your views here.

# class JSONResponse(HttpResponse):
#     def __init__(self,data,**kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)

# @api_view(['GET','POST'])
# def snippet_list(request,format=None):
#     """
#     列出所有的code snippet， 或创建一个新的snippet
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializers(snippets, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = SnippetSerializers(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def snippet_detail(request,pk,format=None):
#     """
#     获取，更新或删除一个code snippet
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)    
#     except  Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = SnippetSerializers(snippet)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = SnippetSerializers(snippet, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#基于APIView编写
# class SnippetList(APIView):
#     def get(self,request,format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializers(snippets, many=True)
#         return Response(serializer.data)

#     def post(self,request,format=None):
#         serializer = SnippetSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SnippetDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise http404

#     def get(self,request,pk,format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializers(snippet)
#         return Response(serializer.data)

#     def put(self,request,pk,format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializers(snippet,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,pk,format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#基于mixin类编写视图

# class SnippetList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializers

#     def get(self,request, *args, **kwargs):
#         return self.list(request,*args,**kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class SnippetDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializers

#     def get(self,request, *args, **kwargs):
#         return self.retrieve(request,*args, ** kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

#rest_framework提供一组已经混合好的通用视图，使用起来更加简洁
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer