# third party library imports
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.throttling import AnonRateThrottle
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from kavenegar import KavenegarAPI
# local library imports
from otp.serializers import (
    RequestOtpSerializer, RequestOtpResponseSerializer
)
from otp.models import OtpRequest


class OncePerMinuteThrottle(AnonRateThrottle):
    rate = "1/minute"


class RequestOtpAPI(APIView):
    throttle_classes = [
        OncePerMinuteThrottle
    ]

    def post(self, request: Request):
        serializer = RequestOtpSerializer(data=request.data)
        if serializer.is_valid():
            otp_request = self._create_otp_request(serializer)
            self._send_sms(otp_request)
            return Response(
                RequestOtpResponseSerializer(otp_request).data
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    @staticmethod
    def _create_otp_request(serializer: RequestOtpSerializer) -> OtpRequest:
        otp_request: OtpRequest = OtpRequest()
        otp_request.phone = serializer.validated_data['phone']
        otp_request.channel = serializer.validated_data['channel']
        otp_request.generate_password()
        otp_request.save()
        return otp_request

    @staticmethod
    def _send_sms(otp_request: OtpRequest) -> None:
        api = KavenegarAPI(settings.SMS_API_KEY)
        api.verify_lookup({
            'receptor': otp_request.phone,
            'token': otp_request.password,
            'template': settings.OTP_TEMPLATE,
        })
