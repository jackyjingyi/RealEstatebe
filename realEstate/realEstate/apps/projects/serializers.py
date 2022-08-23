from rest_framework import serializers
from .models import Protocol1_1, Protocol1_2, Protocol1_3, ProtocolMain


class Protocol1_1Serializers(serializers.ModelSerializer):
    class Meta:
        model = Protocol1_1
        fields = "__all__"


class Protocol1_2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Protocol1_2
        fields = "__all__"


class Protocol1_3Serializers(serializers.ModelSerializer):
    class Meta:
        model = Protocol1_3
        fields = "__all__"


class ProtocolMainSerializers(serializers.ModelSerializer):
    # part1_p1 = Protocol1_1Serializers()
    # part1_p2 = Protocol1_2Serializers()
    # part1_p3 = Protocol1_3Serializers()

    class Meta:
        model = ProtocolMain
        fields = "__all__"
