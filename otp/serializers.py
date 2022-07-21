from rest_framework import serializers
from otp.models import OtpRequest


class RequestOtpSerializer(serializers.Serializer):
    """Request otp serializer

    Args:
        phone (CharField): user phone number
        channel (ChoiceField): user device(android, ios, web)
    """
    phone = serializers.CharField(
        max_length=15,
        allow_null=False
    )
    channel = serializers.ChoiceField(
        choices=['android', 'ios', 'web'],
        allow_null=False
    )


class RequestOtpResponseSerializer(serializers.ModelSerializer):
    """If otp request is valid, return request id
    """
    class Meta:
        model = OtpRequest
        fields = ['request_id']


class VerifyOtpSerializer(serializers.Serializer):
    """Verify otp serializer

    Args:
        request_id (CharField): otp request id
        phone (CharField): user phone number
        password (CharField): request one time password
    """
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
    """if otp request verified, return token and user state
    """
    token = serializers.CharField()
    new_user = serializers.BooleanField()
