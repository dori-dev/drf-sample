"""Otp views
"""
# standard libraries
from django.utils import timezone
from django.contrib.auth import get_user_model
# third party libraries
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.throttling import AnonRateThrottle
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from kavenegar import KavenegarAPI, APIException
# local libraries
from otp.serializers import (
    RequestOtpSerializer, RequestOtpResponseSerializer,
    VerifyOtpSerializer, VerifyOtpResponseSerializer
)
from otp.models import OtpRequest


class OncePerMinuteThrottle(AnonRateThrottle):
    """User can call api 1 time per minute
    """
    rate = "1/minute"


class RequestOtpAPI(APIView):
    throttle_classes = [
        OncePerMinuteThrottle
    ]

    @swagger_auto_schema(
        request_body=RequestOtpSerializer,
        # query_serializer=RequestOtpSerializer,
        responses={
            '200': RequestOtpResponseSerializer,
            '400': 'bad request'
        },
        security=[],
        operation_id='Otp Request',
        operation_description='Request to server for create one time password'
    )
    def post(self, request: Request):
        """post method support for request otp api
        """
        serializer = RequestOtpSerializer(data=request.data)
        if serializer.is_valid():
            otp_request = self._create_otp_request(serializer)
            try:
                self._send_sms(otp_request)
            except APIException:
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
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
        """create otp request object with serializer
        """
        otp_request: OtpRequest = OtpRequest()
        otp_request.phone = serializer.validated_data['phone']
        otp_request.channel = serializer.validated_data['channel']
        otp_request.generate_password()
        otp_request.save()
        return otp_request

    @staticmethod
    def _send_sms(otp_request: OtpRequest) -> None:
        """send sms to phone with kavenegar api
        """
        api = KavenegarAPI(settings.SMS_API_KEY)
        api.verify_lookup({
            'receptor': otp_request.phone,
            'token': otp_request.password,
            'template': settings.OTP_TEMPLATE,
        })


class VerifyOtpAPI(APIView):
    """Verify request id and one time password with phone.
    """

    @swagger_auto_schema(
        request_body=VerifyOtpSerializer,
        # query_serializer=VerifyOtpSerializer,
        responses={
            '200': VerifyOtpResponseSerializer,
            '403': 'wrong data',
            '400': 'bad request'
        },
        security=[],
        operation_id='Otp Verify',
        operation_description='Verify one time password and return token'
    )
    def post(self, request: Request):
        """post method support for verify otp api
        """
        serializer = VerifyOtpSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            if self._verify_data(data):
                token, new_user = self._get_user_info(data)
                return Response(
                    data=VerifyOtpResponseSerializer({
                        'token': token,
                        'new_user': new_user
                    }).data
                )
            else:
                return Response(
                    {"verify": "wrong data!"},
                    status=status.HTTP_403_FORBIDDEN
                )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    @staticmethod
    def _verify_data(data: dict):
        """verify request id, phone and password
        if it object exists in return True and means
        its verified, else return False
        """
        query = OtpRequest.objects.filter(
            request_id=data['request_id'],
            phone=data['phone'],
            password=data['password'],
            valid_until__gte=timezone.now()
        )
        if query.exists():
            return True
        return False

    @staticmethod
    def _get_user_info(data: dict) -> tuple:
        """get user token and user state(new user)
        """
        User = get_user_model()
        user_query = User.objects.filter(
            username=data['phone']
        )
        if user_query.exists():
            user = user_query.first()
            new_user = False
        else:
            user = User.objects.create(
                username=data['phone']
            )
            new_user = True
        token, _ = Token.objects.get_or_create(
            user=user
        )
        return token, new_user
