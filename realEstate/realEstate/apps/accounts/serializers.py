from rest_framework import serializers
from .models import User, IAMUser


class UserSerializer(serializers.ModelSerializer):
    # 前台展示用
    class Meta:
        model = User
        exclude = ['secret_key', 'iam_account', 'iam_password','password']


class UserUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
