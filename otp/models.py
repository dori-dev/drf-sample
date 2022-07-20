# standard libraries
from random import choices
from string import digits
from datetime import timedelta
import uuid
# third party libraries
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


def two_min_until(cls):
    return timezone.now() + timedelta(seconds=120)


class User(AbstractUser):
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class Profile(models.Model):
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


class OtpRequest(models.Model):
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
    receipt_id = models.CharField(
        max_length=255,
        null=True
    )

    def generate_password(self):
        self.password = self._random_password(4)
        self.valid_until = timezone.now() + timedelta(seconds=120)

    @staticmethod
    def _random_password(length: int) -> str:
        return "".join(choices(digits, k=length))

    class Meta:
        verbose_name = _('One Time Password')
        verbose_name_plural = _('One Time Passwords')
