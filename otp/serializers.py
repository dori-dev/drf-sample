from rest_framework import serializers
from otp.models import OtpRequest


class RequestOtpSerializer(serializers.Serializer):
    phone = serializers.CharField(
        max_length=15,
        allow_null=False
    )
    channel = serializers.ChoiceField(
        choices=['android', 'ios', 'web'],
        allow_null=False
    )


class RequestOtpResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtpRequest
        fields = ['request_id']


class VerifyOtpSerializer(serializers.Serializer):
    request_id = serializers.CharField(
        max_length=64,
        allow_null=False
    )
    phone = serializers.CharField(
        max_length=15,
        allow_null=False
    )
    password = serializers.CharField(
        allow_null=False
    )


class VerifyOtpResponseSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_user = serializers.BooleanField()
