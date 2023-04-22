from rest_framework import viewsets
from .models import UserInfo
from .serializer import UserInfoSerializer
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema

class UserInfoViewSet(viewsets.ModelViewSet):

    # モデルのオブジェクトを取得
    queryset = UserInfo.objects.all()

    # シリアライザーを取得
    serializer_class = UserInfoSerializer

    @swagger_auto_schema(operation_description="アイテムの一覧を取得します。")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="新しいアイテムを作成します。")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="指定されたアイテムを取得します。")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="指定されたアイテムを更新します。")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="指定されたアイテムを部分的に更新します。")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="指定されたアイテムを削除します。")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)