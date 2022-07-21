"""Otp models"""
# standard libraries
from random import choices
from string import digits
from datetime import timedelta, datetime
import uuid
# third party libraries
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


def two_min_until() -> datetime:
    """return time of two min after now
    """
    return timezone.now() + timedelta(seconds=120)


class User(AbstractUser):
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class Profile(models.Model):
    """User profile model
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    birth_date = models.DateTimeField(null=True)

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        """When a user is created, a profile is
        automatically created for that user"""
        if created:
            Profile.objects.create(user=instance)

    def __str__(self):
        return f"{self.user.username} profile"


class OtpRequest(models.Model):
    """Otp request model

    Fields:
        request_id (UUIDField): random uuid for request
        channel (CharField): user device
        phone (CharField): user phone number
        password (CharField): user one time password
        valid_from (DateTimeField): time of when the user requested
        valid_until (DateTimeField): As long as the user request id valid
    """
    class OtpChannel(models.TextChoices):
        ANDROID = _("android")
        IOS = _("ios")
        WEB = _("web")

    request_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    channel = models.CharField(
        _("channel"),
        choices=OtpChannel.choices,
        max_length=12,
    )
    phone = models.CharField(
        max_length=15
    )
    password = models.CharField(
        max_length=4,
        null=True
    )
    valid_from = models.DateTimeField(
        default=timezone.now
    )
    valid_until = models.DateTimeField(
        default=two_min_until
    )

    def generate_password(self):
        """generate one time password and set valid_until
        """
        self.password = self._random_password(4)
        self.valid_until = timezone.now() + timedelta(seconds=120)

    @staticmethod
    def _random_password(length: int) -> str:
        """generate random password

        Args:
            length (int): password length
        """
        return "".join(choices(digits, k=length))

    def __str__(self):
        return f"{self.phone} otp request."

    class Meta:
        verbose_name = _('OTP Request')
        verbose_name_plural = _('OTP Requests')
