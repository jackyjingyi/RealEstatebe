from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import BuildingProduct, House

user = get_user_model()


class BuildingListSerializer(serializers.ModelSerializer):
    key = serializers.CharField(source="pk")
    display_txt = serializers.SerializerMethodField()

    class Meta:
        model = BuildingProduct
        fields = "__all__"

    @staticmethod
    def get_display_txt(obj):
        return str(obj)


class BuildingCreateUpdateSerializer(serializers.ModelSerializer):
    options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = BuildingProduct
        fields = "__all__"

    @staticmethod
    def get_options_display_txt(obj):
        return str(obj)
