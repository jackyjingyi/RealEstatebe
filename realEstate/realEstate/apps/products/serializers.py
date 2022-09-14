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


class BuildingProductListSerializer(serializers.ModelSerializer):
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()
    region_en = serializers.SerializerMethodField()
    product_type_en = serializers.SerializerMethodField()

    class Meta:
        model = BuildingProduct
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)

    @staticmethod
    def get_region_en(obj):
        if obj.region == '华南战区':
            return 'chinaSouth'
        elif obj.region == '北方战区':
            return 'chinaNorth'
        elif obj.region == '西部战区':
            return 'chinaWest'
        elif obj.region == '华东战区':
            return 'chinaEast'
        elif obj.region == '中部战区':
            return 'chinaMiddle'
        else:
            return None

    @staticmethod
    def get_product_type_en(obj):
        if obj.product_type == '中高层':
            return 'medianBuilding'
        elif obj.product_type == '小高层':
            return 'lowBuilding'
        elif obj.product_type == '高层':
            return 'highBuilding'
        else:
            return None


class BuildingProductCreateUpdateSerializer(serializers.ModelSerializer):
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = BuildingProduct
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = "__all__"


class HouseListSerializer(serializers.ModelSerializer):
    class BuildingProductSerializer(serializers.ModelSerializer):
        ty_options_display_txt = serializers.SerializerMethodField()

        class Meta:
            model = BuildingProduct
            fields = "__all__"

        @staticmethod
        def get_ty_options_display_txt(obj):
            return str(obj)

    building = BuildingProductSerializer()
    key = serializers.CharField(source="pk")
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = House
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)


class HouseCreateUpdateSerializer(serializers.ModelSerializer):
    ty_options_display_txt = serializers.SerializerMethodField()

    class Meta:
        model = House
        fields = "__all__"

    @staticmethod
    def get_ty_options_display_txt(obj):
        return str(obj)
