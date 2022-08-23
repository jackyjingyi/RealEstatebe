from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import ManagementFiles, Materials


class ManagementFilesSerializer(serializers.ModelSerializer):
    key = serializers.CharField(source="pk")
    file_path = serializers.CharField(source='file.url', read_only=True)
    file_name = serializers.CharField(source='file.name', read_only=True)
    download_file_path = serializers.SerializerMethodField()
    download_file_name = serializers.SerializerMethodField()

    class Meta:
        model = ManagementFiles
        fields = "__all__"

    def get_download_file_name(self, obj):
        try:
            return obj.download_file.name
        except ValueError:
            return ''

    def get_download_file_path(self, obj):
        try:
            return obj.download_file.url
        except ValueError:
            return ''


class MaterialsSerializers(serializers.ModelSerializer):
    ke = serializers.CharField(source="pk")
    file_path = serializers.CharField(source='file.url', read_only=True)
    file_name = serializers.CharField(source='file.name', read_only=True)

    class Meta:
        model = Materials
        fields = "__all__"
