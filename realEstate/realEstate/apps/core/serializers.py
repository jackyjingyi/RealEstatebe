from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import ManagementFiles

class ManagementFilesSerializer(serializers.ModelSerializer):
    key = serializers.CharField(source="pk")
    file_path = serializers.CharField(source='file.url', read_only=True)
    class Meta:
        model = ManagementFiles
        fields = "__all__"


